from django.db import models
from django.contrib.auth.models import User

class Categorias(models.Model):
    nombre = models.CharField(max_length='100', unique=True)
    registro =  models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, null=True)
    def __unicode__(self):
        return self.nombre
    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'Categorias'

class Tipo(models.Model):
    nombre = models.CharField(max_length='100', unique=True)
    registro =  models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categorias, null=True)
    def __unicode__(self):
        return self.categoria.nombre + " - " + self.nombre
    class Meta:
        ordering = ['categoria']
        verbose_name_plural = 'Tipos'

class Productos(models.Model):
    nombre = models.CharField(max_length='100')
    descripcion = models.TextField()
    registro = models.DateTimeField(auto_now_add=True)
    tipo = models.ManyToManyField(Tipo)
    usuario = models.ForeignKey(User, unique=True)
    def __unicode__(self):
        return self.nombre