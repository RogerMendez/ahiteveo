from django.forms import ModelForm, Textarea
from productos.models import Categorias, Productos

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
