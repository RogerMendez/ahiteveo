from django.forms import ModelForm, Textarea, TextInput
from django import forms
from productos.models import Categorias, Productos, Tipo, Imagenes

class CategoriaForm(ModelForm):
    class Meta:
        model = Categorias
        exclude = ['usuario', 'estado']

class ProductoForm(ModelForm):
    class Meta:
        model = Productos
        exclude = ['usuario']
        widgets = {
            'descripcion':Textarea(attrs={'class':'form-control'}),
            }
class ProductoSearch(forms.Form):
    texto = forms.CharField(max_length='100', widget=TextInput(attrs={
        'class':'form-control',
        'placeholder':'Nombre de Producto',
    }))

class TipoForm(ModelForm):
    class Meta:
        model = Tipo
        exclude = ['estado']

class ImagenesForm(ModelForm):
    class Meta:
        model = Imagenes
        exclude = ['producto']