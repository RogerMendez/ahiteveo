from django import forms
from django.forms import ModelForm

from users.models import Perfiles

class EmailForm(forms.Form):
	email = forms.EmailField(label='Correo Electronico')

class PerfilForm(ModelForm):
	class Meta:
		model = Perfiles
		exlucde = ['usuario', 'nacionalidad']