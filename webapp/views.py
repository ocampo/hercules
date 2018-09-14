from django.shortcuts import render
from .models import Proveedor, Producto, Lista, Zona, Unidad
from .hercules import *
from django.http.response import JsonResponse

# HOME
def home(request):
    return render(request, 'webapp/home.html', {})

def requisicion(request):
    return render(request, 'webapp/requisicion.html', {})

def compras(request):
    return render(request, 'webapp/compras.html', {})

def cervecera(request):
    return render(request, 'webapp/cervecera.html', {})

def upload(request):
    return render(request, 'webapp/upload.html', {})

def usuarios(request):
    return render(request, 'admin', {})

def analitica(request):
    return render(request, 'webapp/analitica.html', {})

def nuevar(request):
    return render(request, 'webapp/nuevar.html',{})

def cproductos(request):
    proveedor = request.GET.get('proveedor')
    zona = request.GET.get('zona')
    contenido = Productos.objects.filter(proveedor=proveedor)
    context = {'contenido':contenido,'proveedor':proveedor}

def cproveedores(request):
    zona = request.GET.get('zona')
    nivel = request.GET.get('nivel')
    if zona == 'cacomixtle':
        contenido = Proveedor.objects.filter(c=True,active=True)
    if zona == 'plantaalta':
        contenido = Proveedor.objects.filter(pa=True,active=True)
    if zona == 'barra':
        contenido = Proveedor.objects.filter(b=True,active=True)
    if zona == 'bplantaalta':
        contenido = Proveedor.objects.filter(bpa=True,active=True)
    context = {'contenido':contenido,'zona':zona}
    print(request.__dict__)
    return render(request, 'webapp/cproveedores.html', context)

def cproductos(request):
    proveedor = request.GET.get('proveedor')
    productos = Producto.objects.filter(proveedor_id=proveedor,active=True)
    contenido = productos
    zona = request.GET.get('zona')
    context = {"contenido":contenido,"zona":zona}
    return render(request, 'webapp/cproductos.html', context)

def lista(request):
    lista = Lista.objects.all()
    print(lista)
    contenido = generador_lista(lista)
    return render(request, 'webapp/lista.html', {"contenido":contenido})

def ajax(request):
    print("en ajax")
    if proceso == "agregaralista":
        proceso = request.GET.get("proceso")
        proveedor = request.GET.get("proveedor")
        print("va")
        print(proveedor)
        p_id = Producto.objects.filter(proveedor_id=proveedor).values('proveedor_id')[0]['proveedor_id']
        zona = Proveedor.objects.filter(id=p_id).values('zone_id')[0]['zone_id']
        producto = request.GET.get("producto")
        unidad = request.GET.get("unidad")
        print("va la unidad %c "% unidad)
        unidad = Unidad.objects.get(pk=int(unidad)).nombre
        numero = request.GET.get("numero")
        nuevo = Lista.objects.create(proveedor=proveedor,zona=zona,pagado=False,producto=producto,cantidad=numero,unidad=unidad)
        nuevo.save()
        print("se agregó a lista")
        return JsonResponse({"success":True})
    elif proceso == "updatelista":
        done = request.POST.get("done")
        list_id = request.POST.get("id")
        Lista.objects.filter(pk=list_id).update(done=done)
