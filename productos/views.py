#encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, AdminPasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_unicode
from django.contrib.admin.models import LogEntry, ADDITION
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.contrib import messages

from productos.models import Categorias
from productos.form import CategoriaForm, ProductoForm

def admin_log_addnition(request, objecto, mensaje):
    LogEntry.objects.log_action(
                user_id         = request.user.pk,
                content_type_id = ContentType.objects.get_for_model(objecto).pk,
                object_id       = objecto.pk,
                object_repr     = force_unicode(objecto),
                action_flag     = ADDITION,
                change_message = mensaje,
            )

def index(request):
    categorias = Categorias.objects.all()
    return render(request, 'categorias/index.html', {
        'categorias':categorias,
    })

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