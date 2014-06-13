from django.contrib import admin
from productos.models import Tipo, Categorias, Productos

admin.site.register(Categorias)
admin.site.register(Tipo)
admin.site.register(Productos)
