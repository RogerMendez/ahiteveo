# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Perfiles(models.Model):
    fecha_nac = models.DateField(verbose_name="Fecha de Nacimiento", help_text=u"DIA/MES/AÑO", null=True, blank=True)
    telefono = models.IntegerField(max_length='10', verbose_name="Telefono/Celular", null=True, blank=True)
    sex = (
        ('FE', 'Femenino'),
        ('MA', 'Masculino'),
    )
    sexo = models.CharField(max_length=2, choices=sex, verbose_name="Sexo", null=True, blank=True)
    naci = (
        ('Boliviana', 'Boliviana'),
    )
    nacionalidad = models.CharField(max_length=15, default="Boliviana", choices=naci, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatar', verbose_name="Seleccionar Imagen", blank=True, null=True)
    completo = models.BooleanField(default=False)
    code_activation = models.CharField(max_length="100")
    usuario = models.ForeignKey(User, null=True, blank=True, unique=True)
    def __unicode__(self):
        return self.nombre + " " + self.paterno + " " + self.materno
    class Meta:
        verbose_name_plural = "Perfiles"      