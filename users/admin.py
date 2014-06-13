from django.contrib import admin
from users.models import Ciudad, Pais, Perfil
# Register your models here.

admin.site.register(Pais)
admin.site.register(Ciudad)
admin.site.register(Perfil)