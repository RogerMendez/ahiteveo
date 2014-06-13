from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
# Create your models here.
t = (
    ('Empresa', 'Empresa'),
    ('Personal', 'Personal'),
)

User.add_to_class('code_activation', models.CharField(max_length="100", null=True, blank=True))
User.add_to_class('tipo', models.CharField(max_length='10', choices=t, null=True, blank=True))

class Pais(models.Model):
    nombre = models.CharField(max_length='100')
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = 'Paices'
        ordering = ['nombre']

class Ciudad(models.Model):
    nombre = models.CharField(max_length='100')
    pais = models.ForeignKey(Pais)
    def __unicode__(self):
        return self.pais.nombre + ' - ' + self.nombre
    class Meta:
        verbose_name_plural = 'Ciudades'

class Perfil(models.Model):
    avatar = models.ImageField(upload_to='avatar')
    telefono = models.CharField(max_length='10')
    direccion = models.CharField(max_length='100')
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento", null=False, default=None)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True)
    ciudad = models.ForeignKey(Ciudad, null=True, blank=True)
    def __unicode__(self):
        return self.user.username

