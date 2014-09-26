from django.shortcuts import render
from django.template import RequestContext
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
from django.core.mail import EmailMultiAlternatives
from users.forms import EmailForm, PerfilForm, UserForm
from users.models import Perfil
# Create your views here.
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
    return render(request, 'base.html')

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
            p = Perfil.objects.create(
                code_activation = code,
                usuario = u,
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
    return render(request, 'users/new_user.html', {
        'formuser':formuser,
        'formemail':formemail,
    })

def confirmation_user(request):
    code = request.GET['code']
    if Perfil.objects.filter(code_activation = code):
        p = Perfil.objects.get(code_activation = code)
        u = User.objects.get(pk = p.usuario_id)
        u.is_active = True
        p.code_activation += u.username
        p.save()
        u.save()
        msm = 'Su cuenta fue Activada Correctamente'
        messages.add_message(request, messages.INFO, msm)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect(reverse(new_user))

def loguet_in(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect(reverse(perfil))
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
                        msm = "Inicio de Sesion Correcto <strong>Gracias Por Su Visita</strong>"
                        messages.add_message(request, messages.INFO, msm)
                        return HttpResponseRedirect(str(request.GET['next']))
                    else:
                        msm = "Inicio de Sesion Existoso <strong>Gracias Por Su Visita</strong>"
                        messages.add_message(request, messages.SUCCESS, msm)
                        return HttpResponseRedirect(reverse(perfil))
                else:
                    sms = "Su Cuenta No Esta Activada <strong>Verifique su Correo Electronico Para Activar La Cuenta</strong>"
                    messages.warning(request, sms)
                    return HttpResponseRedirect(reverse(loguet_in))
            else:
                msm = "Usted No Es Usuario Del Sistema - <strong>Registrate</strong>"
                messages.add_message(request, messages.ERROR, msm)
                return HttpResponseRedirect(reverse(loguet_in))
    else:
        formulario = AuthenticationForm()
    return render(request, 'users/login.html',{
        'formulario':formulario
    })

@login_required(login_url='/login')
def loguet_out(request):
    msm = "Sesion Terminada Correctamente <strong>Vuelva Pronto</strong>"
    messages.add_message(request, messages.INFO, msm)
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/login')
def reset_pass(request):
    if request.method == 'POST' :
        formulario = AdminPasswordChangeForm(user=request.user, data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect(reverse(loguet_in))
    else:
        formulario = AdminPasswordChangeForm(user=request.user)
    return  render(request, 'users/reset_pass.html', {
        'formulario' :formulario
    })

@login_required(login_url='/login')
def index_perfil(request):
    return render(request, 'users/index.html')


@login_required(login_url='/login')
def complete_perfil(request):
    perfil = Perfil.objects.get(usuario = request.user)
    if request.method == 'POST':
        formperfil = PerfilForm(request.POST, request.FILES, instance=perfil)
        formuser = UserForm(request.POST, instance=request.user)
        if formuser.is_valid() and formperfil.is_valid():
            p = formperfil.save()
            u = formuser.save()
            #p.user = request.user
            #p.save()
            msm = "Perfil Completado Correctamente"
            messages.add_message(request, messages.INFO, msm)
            return HttpResponseRedirect(reverse(index_perfil))
    else:
        formperfil = PerfilForm(instance=perfil)
        formuser = UserForm(instance=request.user)
    return render(request, 'users/new_perfil.html', {
        'formperfil':formperfil,
        'formuser':formuser,
    })

@login_required(login_url='/login')
def edit_perfil(request):
    per = Perfil.objects.get(usuario = request.user)
    if request.method == 'POST':
        formperfil = PerfilForm(request.POST, request.FILES, instance=per)
        formuser = UserForm(request.POST, instance=request.user)
        if formuser.is_valid() and formperfil.is_valid():
            p = formperfil.save()
            u = formuser.save()
            p.user = request.user
            p.save()
            msm = "Perfil Completado Correctamente"
            messages.add_message(request, messages.INFO, msm)
            return HttpResponseRedirect(reverse(index_perfil))
    else:
        formperfil = PerfilForm(instance=per)
        formuser = UserForm(instance=request.user)
    return render(request, 'users/edit_perfil.html', {
        'formperfil':formperfil,
        'formuser':formuser,
    })