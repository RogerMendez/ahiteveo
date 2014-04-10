from django.db import models
from django.db.models import User

from djangotoolbox.fields import ListField

class Persona(models.Model):
    paterno = models.CharField(max_length='50', verbose_name="Apellido Paterno")
    materno = models.CharField(max_length='50', null=True, blank=True, verbose_name="Apellido Materno")
    nombre = models.CharField(max_length='100', verbose_name="Nombres")
    fecha_nac = models.DateField(verbose_name="Fecha de Nacimiento", help_text="DIA/MES/AÑO", null=True, blank=True)
    direccion = models.CharField(max_length='100', null=True, blank=True, verbose_name="Dirección de Empleado")
    telefono = models.IntegerField(max_length='10', verbose_name="Telefono/Celular", null=True, blank=True)
    estado_civ = (
        ('SO', 'Soltero(a)'),
        ('CA', 'Casado(a)'),
    )
    estado_civil = models.CharField(max_length='2',choices=estado_civ, null=True, blank=True, verbose_name="Estado Civil")
    sex = (
        ('FE', 'Femenino'),
        ('MA', 'Masculino'),
    )
    sexo = models.CharField(max_length=2, choices=sex, verbose_name="Sexo", null=True, blank=True)
    naci = (
        ('Boliviana', 'Boliviana'),
    )
    nacionalidad = models.CharField(max_length=15, default="Boliviana", choices=naci, null=True, blank=True)
    foto = models.ImageField(upload_to='personal', verbose_name="Seleccionar Imagen", blank=True, null=True)
    completo = models.BooleanField(default=False)
    code_activation = models.CharField(max_length="100")
    usuario = models.ForeignKey(User, null=True, blank=True, unique=True)
    def __unicode__(self):
        return self.nombre + " " + self.paterno + " " + self.materno
    class Meta:
        ordering = ["ci"]
        verbose_name_plural = "Empleados"