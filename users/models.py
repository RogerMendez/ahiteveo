from django.db import models
from django.contrib.auth.models import User

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
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento", null=True)
    t = (
        ('Empresa', 'Empresa'),
        ('Personal', 'Personal'),
    )
    code_activation = models.CharField(max_length="100", null=True, blank=True)
    tipo = models.CharField(max_length='10', choices=t, null=True, blank=True)
    usuario = models.OneToOneField(User, null=True)
    ciudad = models.ForeignKey(Ciudad, null=True, blank=True)
    time = models.DateTimeField(null = True)
    def __unicode__(self):
        return self.usuario.username
    def edad(self):
        import datetime
        return self.fecha_nacimiento - datetime.datetime.now()
