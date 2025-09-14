# 2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos=[]

for i in range(5):
    producto=input(f"ingrese el producto {i+1}: ")
    productos.append(producto)
print("Lista de productos ordenada alfabéticamente:")
print(sorted(productos))

producto_eliminar=input("Ingrese el producto que desea eliminar: ")
if producto_eliminar in productos:
    productos.remove(producto_eliminar)
    print("Producto eliminado. Lista actualizada:")
    print(productos)
else:
    print("El producto no se encuentra en la lista.")
