from django import forms
from django.forms import ModelForm, DateInput, Textarea, TextInput
from users.models import Perfil
from django.contrib.auth.models import User

class EmailForm(forms.Form):
	email = forms.EmailField(label='Correo Electronico', widget=(forms.EmailInput()))


class PerfilForm(ModelForm):
    class Meta:
        model = Perfil
        exclude = ['user']
        widgets = {
            'fecha_nacimiento':TextInput(attrs={'type':'date'}),
            }

class UserForm(ModelForm):
    class Meta:
        model = User
        exclude = ['username', 'password', 'is_staff', 'is_superuser', 'last_login', 'is_active', 'date_joined', 'user_permissions', 'groups', 'email', 'code_activation']
        fields = ('tipo', 'first_name', 'last_name')