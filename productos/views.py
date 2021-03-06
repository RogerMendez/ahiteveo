#encoding:utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.template import RequestContext
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, AdminPasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_unicode
from django.contrib.admin.models import LogEntry, ADDITION
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.contrib import messages

from productos.models import Categorias, Tipo, Productos, Imagenes
from productos.form import CategoriaForm, ProductoForm, TipoForm, ImagenesForm

def admin_log_addnition(request, objecto, mensaje):
    LogEntry.objects.log_action(
                user_id         = request.user.pk,
                content_type_id = ContentType.objects.get_for_model(objecto).pk,
                object_id       = objecto.pk,
                object_repr     = force_unicode(objecto),
                action_flag     = ADDITION,
                change_message = mensaje,
            )

@login_required(login_url='/login')
def index(request):
    categorias = Categorias.objects.all()
    productos = Productos.objects.all()

    return render(request, 'categorias/index.html', {
        'categorias':categorias,
        'productos': productos,
    })

@login_required(login_url='/login')
def new_categoria(request):
    categorias = Categorias.objects.all()
    if request.method == 'POST':
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
            c = formulario.save()
            c.usuario = request.user
            c.save()
            admin_log_addnition(request, c, 'Creacion Categoria')
            msm = u"Se Añadio con Exito la Categoria <strong>" + c.nombre + "</strong>"
            messages.add_message(request, messages.INFO, msm)
            return HttpResponseRedirect(reverse(index))
    else:
        formulario = CategoriaForm()
    return render(request, 'categorias/new_category.html', {
        'formulario':formulario,
        'categorias':categorias,
    })

@login_required(login_url='/login')
def new_tipo(request):
    if request.method == 'POST':
        formulario = TipoForm(request.POST)
        if formulario.is_valid():
            e = formulario.save()
            admin_log_addnition(request, e, 'Tipo Creado')
            sms = "Tipo <strong>%s</strong> Registrado Correctamente"% e.nombre
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(index))
    else:
        formulario = TipoForm()
    return render(request, 'categorias/new_tipo.html',{
        'formulario':formulario,
    })


@login_required(login_url='/login')
def index_productos(request):
    productos = Productos.objects.filter(usuario = request.user)
    imagenes = Imagenes.objects.filter(producto = productos)
    formulario = ImagenesForm()
    return render(request, 'productos/index.html',{
        'productos':productos,
        'imagenes':imagenes,
        'formulario':formulario,
    })

def imagenes_producto_ajax(request):
    if request.is_ajax():
        id = request.GET['id']
        producto = get_object_or_404(Productos, pk = id)
        imagenes = Imagenes.objects.filter(producto = producto)
        html = render_to_string('productos/ajax/imagenes_ajax.html', {
            'producto':producto,
            'imagenes':imagenes,
        }, context_instance=RequestContext(request))
        print html
        return JsonResponse(html, safe=False)
    else:
        raise Http404

@login_required(login_url='/login')
def new_producto(request):
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES)
        if formulario.is_valid():
            p = formulario.save()
            p.usuario = request.user
            p.save()
            sms = "Producto %s Creado Correctamente"% (p.nombre)
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(index_productos))
    else:
        formulario = ProductoForm()
    return render(request, 'productos/new_producto.html', {
        'formulario':formulario,
    })

@login_required(login_url='login')
def update_producto(request, id_producto):
    producto = get_object_or_404(Productos, pk = id_producto)
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES, instance=producto)
        if formulario.is_valid():
            p = formulario.save()
            sms = "Producto %s Modificado Correctamente"% (p.nombre)
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(index_productos))
    else:
        formulario = ProductoForm(instance=producto)
    return render(request, 'productos/update_producto.html', {
        'formulario':formulario,
    })

@login_required(login_url='/login')
def new_imagen(request, producto_id):
    producto = get_object_or_404(Productos, pk = producto_id)
    if request.method == "POST":
        formulario = ImagenesForm(request.POST, request.FILES)
        if formulario.is_valid():
            i = formulario.save()
            i.producto = producto
            i.save()
            sms = "Imagen Guardada Correctamente"
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(index_productos))
    return HttpResponseRedirect(reverse(index_productos))