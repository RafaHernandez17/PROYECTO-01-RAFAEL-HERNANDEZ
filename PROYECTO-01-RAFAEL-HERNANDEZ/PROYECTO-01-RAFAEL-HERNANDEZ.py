from numpy import append
from datetime import datetime
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
"""
lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""
#--------------------Login-----------------------------
print(">>>>>>>>>>>>>>>>>>>Login")
usuarios = {
        "odin": {
            "nombre": "Brayan",
            "apellido": "Hernandez",
            "password": "123123"
    },
        "fmuguruza": {
            "nombre": "Fermín",
            "apellido": "Muguruza",
            "password": "654321"
    },
        "aolaizola": {
            "nombre": "Aimar",
            "apellido": "Olaizola",
            "password": "123456"
    }
 }

User = input("Escriba su usuario: ")
Pass = input("Escriba su password: ")
if User in usuarios and Pass == usuarios[User]['password']:
    print("si")
else:
    print("no")
#---------------------------------------------------
"""
1. Productos más vendidos y productos rezagados:
"""
#----------------Mas vendidos----------------

ventasProductos =[]; product =[] 

ventasProductos = [] 

for ventas in lifestore_sales: # Se guardan todos los pruductos vendidios
    ventasProductos.append(ventas[1]) # ventas[1] es igual al id productos
    
for ventas in lifestore_products:
    recolectar = []
    product.append(recolectar)
    for i in range(1): 
        recolectar.append(ventas[0]) # Id
        recolectar.append(ventas[1]) # Nombres
        recolectar.append(ventas[3]) # categorias
        recolectar.append(ventasProductos.count(ventas[0])) # contador de las veces del  productos vendidos
        

product = sorted(product, key=lambda x:x[3]) # ordena la lista respecto al valor de ventas de cada producto
print("---------------- 1.1 - Productos mas vendidos----------------")
for i in [-1, -2, -3, -4, -5]: # imprimos los ultimos valores ya que son los mayores
    print(f'Nombre del Producto: {product[i][1]}\t Numero Total de ventas: {product[i][3]}') # Formato para venlos en pilas

#----------------Busquedas----------------

busquedaProducto = []; busqueda = []

busquedaProducto =[]

for busquedaM in lifestore_searches: # Se guardan todos los pruductos buscados
    busquedaProducto.append(busquedaM[1]) # busquedaM[1] es igual al id productos

for busquedaM in lifestore_products:# creamos una lista donde se van anexar los nombres y busqueda totales de cada producto
    almacenar = []
    busqueda.append(almacenar) # Almacena [name, categoria, numero total de busqueda]
    for i in range(1):
        almacenar.append(busquedaM[1]) # Nombres
        almacenar.append(busquedaM[3]) # Categorias la anexo ya que nos ayuda ahorrar codigo despues
        almacenar.append(busquedaProducto.count(busquedaM[0])) # contador de las veces del  productos vendidos

busqueda = sorted(busqueda, key=lambda x:x[2]) # ordena la lista respecto al valor de busqueda de cada producto
print("---------------- 1.2 - Productos mas buscados----------------")
for i in [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]: # imprimos los ultimos valores ya que son los mayores
    print(f'Nombre del Producto: {busqueda[i][0]}\t Numero Total de busqueda: {busqueda[i][2]}')

#----------------Productos por categoria con menores ventas----------------

Categorias = []

for todasCate in lifestore_products: # creamos un diccionario para tener todas las categorias
    Categorias.append(todasCate[3])

Categorias = list(dict.fromkeys(Categorias))
# print(Categorias)

"""
'procesadores', 'tarjetas de video', 'tarjetas madre', 'discos duros', 'memorias usb', 'pantallas', 'bocinas', 'audifonos'
"""

procesadores = []; tarjetas_video = []; tarjetas_madre = []; discos_duros = []; memorias_usb = []; 
pantallas = []; bocinas =[]; audifonos = []

for i in product: # aqui recorremos en nuestra variable unica
     #que nos ayuda porque ya estan ordenados y acumuladas las ventas, solo es separar por categorias
    if Categorias[0] in i:
        procesadores.append(i[:4])
    elif Categorias[1] in i:
        tarjetas_video.append(i[:4])
    elif Categorias[2] in i:
        tarjetas_madre.append(i[:4])
    elif Categorias[3] in i:
        discos_duros.append(i[:4])
    elif Categorias[4] in i:
        memorias_usb.append(i[:4])
    elif Categorias[5] in i:
        pantallas.append(i[:4])
    elif Categorias[6] in i:
        bocinas.append(i[:4])
    elif Categorias[7] in i:
        audifonos.append(i[:4])

print("---------------- 1.3 - Productos menos vendidos por categorias----------------")

print(">>>>>>> Menos ventas en Procesadores")
for i in range(5): # Recorre en los primeros 5 de cada categoria
    print(f'Nombre del Producto: {procesadores[i][1]}\t Categoria: {procesadores[i][2]}\t Numero Total de venta: {procesadores[i][3]}')

print(">>>>>>> Menos ventas en Tarjetas de video")
for i in range(5): 
    print(f'Nombre del Producto: {tarjetas_video[i][1]}\t Categoria: {tarjetas_video[i][2]}\t Numero Total de venta: {tarjetas_video[i][3]}')

print(">>>>>>> Menos ventas en Tarjetas madre")
for i in range(5): 
    print(f'Nombre del Producto: {tarjetas_madre[i][1]}\t Categoria: {tarjetas_madre[i][2]}\t Numero Total de venta: {tarjetas_madre[i][3]}')

print(">>>>>>> Menos ventas en Disco duros")
for i in range(5): 
    print(f'Nombre del Producto: {discos_duros[i][1]}\t Categoria: {discos_duros[i][2]}\t Numero Total de venta: {discos_duros[i][3]}')

print(">>>>>>> Menos ventas en USB")
for i in range(2): 
    print(f'Nombre del Producto: {memorias_usb[i][1]}\t Categoria: {memorias_usb[i][2]}\t Numero Total de venta: {memorias_usb[i][3]}')

print(">>>>>>> Menos ventas en Pantallas")
for i in range(5): 
    print(f'Nombre del Producto: {pantallas[i][1]}\t Categoria: {pantallas[i][2]}\t Numero Total de venta: {pantallas[i][3]}')

print(">>>>>>> Menos ventas en Bocinas")
for i in range(5): 
    print(f'Nombre del Producto: {bocinas[i][1]}\t Categoria: {bocinas[i][2]}\t Numero Total de venta: {bocinas[i][3]}')

print(">>>>>>> Menos ventas en Audifonos")
for i in range(5): 
    print(f'Nombre del Producto: {audifonos[i][1]}\t Categoria: {audifonos[i][2]}\t Numero Total de venta: {audifonos[i][3]}')

#------------------Productos con menores busquedas------------------
procesadores1 = []; tarjetas_video1 = []; tarjetas_madre1 = []; discos_duros1 = []; memorias_usb1 = []; 
pantallas1 = []; bocinas1 =[]; audifonos1 = []

for i in busqueda: # aqui recorremos en nuestra variable unica
     #que nos ayuda porque ya estan ordenados y acumuladas las ventas, solo es separar por categorias
    if Categorias[0] in i:
        procesadores1.append(i[:3])
    elif Categorias[1] in i:
        tarjetas_video1.append(i[:3])
    elif Categorias[2] in i:
        tarjetas_madre1.append(i[:3])
    elif Categorias[3] in i:
        discos_duros1.append(i[:3])
    elif Categorias[4] in i:
        memorias_usb1.append(i[:3])
    elif Categorias[5] in i:
        pantallas1.append(i[:3])
    elif Categorias[6] in i:
        bocinas1.append(i[:3])
    elif Categorias[7] in i:
        audifonos1.append(i[:3])

print("---------------- 1.4 - Productos menos buscados por categorias----------------")

print(">>>>>>> Menos busquedas en Procesadores")
for i in range(9): # Recorre en los primeros 5 de cada categoria
    print(f'Nombre del Producto: {procesadores1[i][0]}\t Categoria: {procesadores1[i][1]}\t Numero Total de busqueda: {procesadores1[i][2]}')

print(">>>>>>> Menos busquedas en Tarjetas de video")
for i in range(10): 
    print(f'Nombre del Producto: {tarjetas_video1[i][0]}\t Categoria: {tarjetas_video1[i][1]}\t Numero Total de busqueda: {tarjetas_video1[i][2]}')

print(">>>>>>> Menos busquedas en Tarjetas madre")
for i in range(10): 
    print(f'Nombre del Producto: {tarjetas_madre1[i][0]}\t Categoria: {tarjetas_madre1[i][1]}\t Numero Total de busqueda: {tarjetas_madre1[i][2]}')

print(">>>>>>> Menos busquedas en Disco duros")
for i in range(10): 
    print(f'Nombre del Producto: {discos_duros1[i][0]}\t Categoria: {discos_duros1[i][1]}\t Numero Total de busqueda: {discos_duros1[i][2]}')

print(">>>>>>> Menos busquedas en USB")
for i in range(2): 
    print(f'Nombre del Producto: {memorias_usb1[i][0]}\t Categoria: {memorias_usb1[i][1]}\t Numero Total de busqueda: {memorias_usb1[i][2]}')

print(">>>>>>> Menos busquedas en Pantallas")
for i in range(10): 
    print(f'Nombre del Producto: {pantallas1[i][0]}\t Categoria: {pantallas1[i][1]}\t Numero Total de busqueda: {pantallas1[i][2]}')

print(">>>>>>> Menos busquedas en Bocinas")
for i in range(10): 
    print(f'Nombre del Producto: {bocinas1[i][0]}\t Categoria: {bocinas1[i][1]}\t Numero Total de busqueda: {bocinas1[i][2]}')

print(">>>>>>> Menos busquedas en Audifonos")
for i in range(10): 
    print(f'Nombre del Producto: {audifonos1[i][0]}\t Categoria: {audifonos1[i][1]}\t Numero Total de busqueda: {audifonos1[i][2]}')
#---------------------------------------------------
"""
2. Productos por reseña en el servicio:
"""
#---------------------Reseñas---------------------

cont=0
puntacionT = []
promedio =[]

for producto in lifestore_products: # Buscamos id product
    for reseña in lifestore_sales:  # Buscamos id product
        if producto[0] == reseña[1]: # comparamos que ambas id sean igauales
            cont += reseña[2] # para luego sumar sus reseñas 
    puntacionT.append(cont) # se agregan a este arreglo
    cont=0 # se reinicia contador para no afectar otros resultados


for reseña in product: # buscamos el numero de ventas totales para sacar promedio 
    acumular = []
    if reseña[3] > 0: 
        promedio.append(acumular)
        for i in range(1):
            acumular.append(reseña[0])
            acumular.append(reseña[1])
            acumular.append(reseña[3])
            acumular.append(puntacionT[reseña[0]-1]/reseña[3]) # sacamos el promedio de su score

promedio = sorted(promedio, key=lambda x:x[3]) # ordenamos con respecto al promedio de score

print(">>>>>>>>>>Mejores reseñas")
for i in range(-1, -6, -1):
     print( F'Nombre del producto: {promedio[i][1]}\t Reseña: {promedio[i][3]}\t Promedio: {promedio[i][2]}' )

print(">>>>>>>>>>Peores reseñas")
for i in range(5):
     print( F'Nombre del producto: {promedio[i][1]}\t Reseña: {promedio[i][3]}\t Promedio: {promedio[i][2]}' )

"""
3. Total de ingresos y ventas promedio mensuales,
total anual y meses con más ventas al año
"""

#-------------------------Total de ingresos y ventas promedio mensuales, total anual y meses con más ventas al año-------------------------
ventasTotales =0;ventasMensuales = [0]*12; gananciaMes =[0]*12; promedioMes =[]; devolucion = []; devolucionTotal =0

fecha =[]; 

for ventas in lifestore_sales:
    fecha.append(ventas[3])

fecha.sort(key = lambda fecha: datetime.strptime(fecha, '%d/%m/%Y'))

ventaProductos = []
for venta in lifestore_sales:
    ventaProductos.append(venta[1])

for i in range(0, len(lifestore_sales)):
    if int(lifestore_sales[i][4]) == 0:
        ventasTotales += lifestore_products[ventaProductos[i]][2]
        if '/01/' in fecha[i]:
            gananciaMes[0] += lifestore_products[ventaProductos[i]][2]
            ventasMensuales[0] += 1
        elif '/02/' in fecha[i]:
            gananciaMes[1] +=  lifestore_products[ventaProductos[i]][2]
            ventasMensuales[1] += 1
        elif '/03/' in fecha[i]:
            gananciaMes[2] +=  lifestore_products[ventaProductos[i]][2]
            ventasMensuales[2]+= 1
        elif '/04/' in fecha[i]:
            gananciaMes[3] += lifestore_products[ventaProductos[i]][2]
            ventasMensuales[3] += 1
        elif '/05/' in fecha[i]:
            gananciaMes[4] += lifestore_products[ventaProductos[i]][2]
            ventasMensuales[4] += 1
        elif '/06/' in fecha[i]:
            gananciaMes[5] += lifestore_products[ventaProductos[i]][2]
            ventasMensuales[5] += 1
        elif '/07/' in fecha[i]:
            gananciaMes[6] += lifestore_products[ventaProductos[i]][2]
            ventasMensuales[6] += 1
        elif '/08/' in fecha[i]:
            gananciaMes[7] += lifestore_products[ventaProductos[i]][2]
            ventasMensuales[7] += 1
        elif '/09/' in fecha[i]:
            gananciaMes[8] += lifestore_products[ventaProductos[i]][2]
            ventasMensuales[8] += 1
        elif '/10/' in fecha[i]:
            gananciaMes[9] += lifestore_products[ventaProductos[i]][2]
            ventasMensuales[9] += 1
        elif '/11/' in fecha[i]:
            gananciaMes[10] += lifestore_products[ventaProductos[i]][2]
            ventasMensuales[10] += 1
        elif '/12/' in fecha[i]:
            gananciaMes[11] += lifestore_products[ventaProductos[i]][2]
            ventasMensuales[11] += 1
    else:
        devolucion.append(ventaProductos[i])
        devolucionTotal += lifestore_products[ventaProductos[1]][2]

for i in range(12):
    if ventasMensuales[i] > 0:
        promedioMes.append(gananciaMes[i]/ventasMensuales[i])
    else:
        promedioMes.append(0)

mes = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio",
        "Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
probMes = []

for lista in zip(mes, ventasMensuales, gananciaMes, promedioMes):
    probMes.append(lista)

probMes = sorted(probMes, key = lambda x:x[2])

print(">>>>>>>>>>>>>>>>>>>>>>Total de ingresos y ventas promedio mensuales")
for i in [-1, -2, -3, -4, -5]:
    print(f'Mes: {probMes[i][0]}\t Venta total: {probMes[i][1]}\t Ventas por mes:$ {probMes[i][2]}\t Promedio de ventaxMes: {probMes[i][3]}')

probMes = sorted(probMes, key = lambda x:x[1])
print(">>>>>>>>>>>>>>>>>>>>>>Meses con más ventas al año")
for i in [-1, -2, -3, -4, -5]:
    print(f'Mes: {probMes[i][0]}\t Venta total: {probMes[i][1]}\t Ventas por mes:$ {probMes[i][2]}')

print(f">>>>>>>>>>>>>>>>>>>>>>Total anual: $ {ventasTotales}")
