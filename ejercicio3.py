cantidad = int(input("¿Cuantos productos va a registrarse?:"))
lista =[]
for i in range(cantidad):
    num = str(i+1)
    nombre = input("Ingrese el nombre del producto:" + num + "i")
    precio = float(input("Ingrese el preci del producto:" + num + "i"))
    categoria = input("Ingrese la categoria del producto:" + num + "i")

    producto = [nombre, precio, categoria]
    lista.append(producto)

#Cantidad de productos en el catalogo
print(len(lista)) #print(cantidad)

#Precio promedio del catalogo
suma = 0
for producto in lista:
    suma = suma + producto[1]
promedio = suma / cantidad
print("El precio promedio es:", suma / cantidad)
 
#Cantidad de productos que superan el precio promedio del ctaalogo
contador = 0
for producto in lista:
    if producto[1] > promedio:
        contador = contador + 1
print("Cantidad de productos que superan el promedio", contador)

#Producto mas caro
mas_caro = lista[0]
for producto in lista:
    if producto[1]>mas_caro[1]:
        mas_caro = producto
print("El producto mas caro es:", mas_caro)

#Producto mas barato
mas_barato = lista[0]
for producto in lista:
    if producto[1]<mas_caro[1]:
        mas_barato = producto
print("El producto mas barato es:", mas_barato)

#Categoria con mas productos
categorias = []
cantidades = []
for p in lista:
    categoria = p[2]
    if categorias.count(categoria) == 0:
        categorias.append(categoria)
        cantidades.append(0)
    else:
        pos = categorias.index(categoria)
        cantidades[pos] = cantidades[pos] + 1
num_mas_alto = max(cantidades)
pos_num_mas_alto = cantidades.index(num_mas_alto)
categoria_con_mas_productos = categorias[pos_num_mas_alto]
print("categoria con mas productos:",categoria_con_mas_productos)
    

    