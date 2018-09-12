from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('requisicion', views.requisicion, name='requisicion'),
    path('compras', views.compras, name='compras'),
    path('analitica', views.analitica, name='analitica'),
    path('cervecera', views.cervecera, name='cervecera'),
    path('upload', views.upload, name='upload'),
    path('nuevar',views.nuevar,name='nuevarequisicion'),
    path('c-proveedores',views.cproveedores,name='c-proveedores'),
    path('c-productos',views.cproductos,name='c-productos'),
    path('ajax',views.ajax,name='ajax'),
    path('lista',views.lista,name='lista'),
]
