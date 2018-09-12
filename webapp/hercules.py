from .models import Proveedor, Producto, Lista, Zona

def generador_lista(lista):
    zonas = Zona.objects.all()
    output = ''
    for zona in zonas:
        print("for zonas")
        print(lista)
        output += zona.nombre+'<br><br>'
        for item in lista:
            print("for lista")
            print(item)
            print(item.zona)
            print(zona.id)
            if int(item.zona) == int(zona.id):
                print("en")
                print("paso el if de afuera")
                proveedor = Proveedor.objects.get(pk=item.proveedor).nombre_corto
                zona = Zona.objects.get(pk=item.zona)
                if item.done == True:
                    check = '<input type="checkbox" name="done" checked />'
                else:
                    check = '<input type="checkbox" name="done" />'
                output = output+\
                """<tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
            </tr>""" % (check,str(item.producto),str(item.cantidad),str(item.unidad),str(proveedor),str(zona),str(item.fecha_de_solicitud.strftime("%d/%m/%y %l:%M%p")))
    return output
