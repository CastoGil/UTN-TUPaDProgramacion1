# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.
with open("07 Manejo de Archivos/productos.txt", "r",encoding="utf-8") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
        
nuevo_nombre = input("Ingrese el nombre del nuevo producto: ").strip()
nuevo_precio = input("Ingrese el precio del nuevo producto: ").strip()
nueva_cantidad = input("Ingrese la cantidad del nuevo producto: ").strip()

with open("07 Manejo de Archivos/productos.txt", "a") as archivo:
    archivo.write(f"{nuevo_nombre},{nuevo_precio},{nueva_cantidad}\n")
print("Nuevo producto agregado con éxito.")

