# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from jsonfield import JSONField

class Area(models.Model):
    nombre = models.CharField(max_length=100,default='NA')
    def __str__(self):
        return self.nombre

class Insumo(models.Model):
    nombre = models.CharField(max_length=300)
    unidad = models.ForeignKey('Unidad',on_delete=models.PROTECT)
    precio_por_unidad = models.FloatField()
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    usuario = models.ForeignKey('auth.User',on_delete=models.PROTECT)
    nombre = models.CharField(max_length=300)
    unidad = models.ForeignKey('Unidad',on_delete=models.PROTECT)
    precio_por_unidad = models.FloatField()
    min_stock = models.IntegerField()
    max_stock = models.IntegerField()
    area = models.ForeignKey('Area',on_delete=models.PROTECT)
    active = models.BooleanField(default=True)
    proveedor = models.ForeignKey('Proveedor',on_delete=models.PROTECT)
    fecha_de_creacion = models.DateTimeField(
            default=timezone.now)
    fecha_de_actualizacion = models.DateTimeField(
            default=timezone.now)
    status = models.IntegerField()
    relacion_insumo = models.ForeignKey('Insumo',on_delete=models.PROTECT,null=True)

    def actualizar(self):
        self.fecha_de_actualizacion = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre

class Unidad(models.Model):
    class Meta:
        verbose_name_plural = "Unidades"
    nombre = models.CharField(max_length=200)
    conversiones = JSONField(blank=True)
    notas = models.TextField(blank=True)
    def __str__(self):
        return self.nombre

class Zona(models.Model):
    nombre = models.CharField(max_length=200);
    otrocentro = JSONField(blank=True)
    notas = models.TextField(blank=True)
    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    class Meta:
        verbose_name_plural = "Proveedores"
    nombre = models.CharField(max_length=200)
    nombre_corto = models.CharField(max_length=60,default='')
    zone = models.ForeignKey('Zona',on_delete=models.PROTECT,default=0)
    RFC = models.CharField(max_length=13)
    calificacion = models.FloatField(blank=True)
    notas = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    c = models.BooleanField(default=False,verbose_name='Cacomixtle')
    b = models.BooleanField(default=False,verbose_name='Barra Jardín')
    pa = models.BooleanField(default=False,verbose_name='Planta Alta')
    bpa = models.BooleanField(default=False,verbose_name='Barra Planta Alta')
    fecha_de_creacion = models.DateTimeField(
            default=timezone.now)
    fecha_de_actualizacion = models.DateTimeField(
            default=timezone.now)
    def __str__(self):
        return self.nombre

class Requisicion(models.Model):
    class Meta:
        verbose_name_plural = "Requisiciones"
    fecha = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey('auth.User',on_delete=models.PROTECT)
    proceso = models.CharField(max_length=10)
    def __str__(self):
        return self.nombre

class Lista(models.Model):
    class Meta:
        verbose_name_plural = "Listas"
    fecha_de_solicitud = models.DateTimeField(default=timezone.now)
    producto = models.CharField(max_length=200)
    cantidad = models.FloatField(default=0)
    unidad = models.CharField(max_length=200,default='')
    zona = models.CharField(max_length=100,default='')
    proveedor = models.CharField(max_length=200,default='')
    done = models.BooleanField(default=False)
    pagado = models.BooleanField(default=False)
