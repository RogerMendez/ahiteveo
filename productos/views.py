#encoding:utf-8
from django.shortcuts import render
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

from productos.models import Categorias, Tipo
from productos.form import CategoriaForm, ProductoForm, TipoForm

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
    return render(request, 'categorias/index.html', {
        'categorias':categorias,
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


def buscar_tipo_ajax(request):
    if request.is_ajax():
        nombre = request.GET['nombre'];
        tipos = Tipo.objects.filter(categoria__nombre = nombre)
        html = render_to_string('categorias/ajax/buscar_tipo_ajax.html',{
            'tipos':tipos,
        }, context_instance=RequestContext(request))
        #html = "hola"
        return JsonResponse(html, safe=False)
    else:
        raise Http404




@login_required(login_url='/login')
def new_producto(request):

    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            p = formulario.save()
            p.usuario = request.user
            p.save()
            return HttpResponseRedirect(reverse(index))
    else:
        formulario = ProductoForm()
    return render(request, 'productos/new_producto.html', {
        'formulario':formulario,

    })