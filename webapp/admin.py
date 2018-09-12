from django.contrib import admin
from .models import *

admin.site.site_header = "Inventarios de Hércules"
admin.site.site_title = "Inventarios de Hércules"

admin.site.register(Producto)
admin.site.register(Insumo)
admin.site.register(Unidad)
admin.site.register(Proveedor)
admin.site.register(Requisicion)
admin.site.register(Zona)
admin.site.register(Area)
