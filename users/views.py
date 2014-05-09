#encoding:utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AdminPasswordChangeForm, AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required
from models import Perfiles
from users.form import EmailForm
from django.core.mail import EmailMultiAlternatives
from django.utils.encoding import force_unicode
from django.contrib.admin.models import LogEntry, ADDITION
from django.contrib.contenttypes.models import ContentType


import random

def admin_log_addnition(request, objecto, mensaje):
    LogEntry.objects.log_action(
                user_id         = request.user.pk,
                content_type_id = ContentType.objects.get_for_model(objecto).pk,
                object_id       = objecto.pk,
                object_repr     = force_unicode(objecto),
                action_flag     = ADDITION,
                change_message = mensaje
            )

def code_activation_create():
    li = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','1','2','3','4','5','6','7','8','9','0']
    #51 elementos
    code = random.choice(li)
    for i in range(50):
        code += random.choice(li)
    return code

def home(request):
    return render_to_response('main.html', context_instance=RequestContext(request))

def loguet_in(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect(reverse(private))
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    if 'next' in request.GET:
                        return HttpResponseRedirect(str(request.GET['next']))
                    else:
                        return HttpResponseRedirect(reverse(private))
                else:
                    return render_to_response('user/noactivo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('user/nousuario.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('user/user_login.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/login')
def loguet_out(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/login')
def private(request) :
    usuario = request.user
    return render_to_response('user/privado.html', {'usuario' :usuario}, context_instance=RequestContext(request))


@login_required(login_url='/login')
def reset_pass(request):
    if request.method == 'POST' :
        formulario = AdminPasswordChangeForm(user=request.user, data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect(reverse(loguet_in))
    else:
        formulario = AdminPasswordChangeForm(user=request.user)
    return  render_to_response('user/reset_pass.html', {'formulario' :formulario}, context_instance=RequestContext(request))


def new_user(request):
    if request.method == 'POST':
        formuser = UserCreationForm(request.POST)
        formemail = EmailForm(request.POST)
        if formemail.is_valid() and formuser.is_valid() :
            code = code_activation_create()
            email = formemail.cleaned_data['email']
            u = formuser.save()
            u.email = email
            u.is_active = False
            u.save()
            per = Perfiles.objects.create(
                usuario = u,
                code_activation = code,
            )
            subject = 'Confirmacion De Correo Electronico'
            text_content = 'Mensaje...nLinea 2nLinea3'
            html_content = '<h2>Confirmacion de Correo</h2><p>Haga click en el siguiente Enlace</p><p><a href="http://127.0.0.1:8000/user/confirmar/?code='+code+'">Confirmar Cuenta</a></p>'
            from_email = '"AhiTeVeo" <sieboliva@gmail.com>'
            to = email
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            msm = "Su Cuenta fue creada Correctamente<br><h2>Un Mensaje fue enviado a su correo para activar su cuenta</h2>"
            messages.add_message(request, messages.INFO, msm)
            return HttpResponseRedirect('/')
    else:
        formuser = UserCreationForm()
        formemail = EmailForm()
    return render_to_response('user/new_user.html',{
        'formuser':formuser,
        'formemail':formemail,
        },context_instance=RequestContext(request))

def confirmation_user(request):
    code = request.GET['code']
    if Perfiles.objects.filter(code_activation = code):
        perfil = Perfiles.objects.get(code_activation = code)
        usuario = User.objects.get(perfiles__code_activation = code)
        usuario.is_active = True
        usuario.save()
        perfil.code_activation += usuario.username
        perfil.save()
        msm = 'Su cuenta fue Activada Correctamente<br><p><a href="http://127.0.0.1:8000/login">Iniciar Sesion</a></p>'
        messages.add_message(request, messages.INFO, msm)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect(reverse(new_user))
