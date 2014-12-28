from django import forms
from django.forms import ModelForm, DateInput, Textarea, TextInput
from users.models import Perfil
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def validar_email(value):
    if User.objects.filter(email = value):
        raise ValidationError(u'Este Correo Electronico ya Esta Registrado')

class EmailForm(forms.Form):
	email = forms.EmailField(label='Correo Electronico', validators=[validar_email], widget=(forms.EmailInput()))


class PerfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'
        exclude = ['usuario', 'code_activation', 'time']
        widgets = {
            'fecha_nacimiento':TextInput(attrs={'type':'date'}),
            }

class PerfilEditForm(ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'
        exclude = ['usuario', 'code_activation', 'tipo', 'time']
        widgets = {
            'fecha_nacimiento':TextInput(attrs={'type':'date'}),
            }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        exclude = ['username', 'password', 'is_staff', 'is_superuser', 'last_login', 'is_active', 'date_joined', 'user_permissions', 'groups', 'email']
