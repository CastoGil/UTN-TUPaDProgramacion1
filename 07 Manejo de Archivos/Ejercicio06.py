# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista.
productos = []
with open("07 Manejo de Archivos/productos.txt", "r",encoding="utf-8") as archivo: 
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)
        
print("Productos actuales:")
for producto in productos:
    print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
    
print("\nAgreguemos un nuevo producto.")
nuevo_nombre = input("Ingrese el nombre del nuevo producto: ").strip().capitalize()
nuevo_precio= float(input("Ingrese el precio del nuevo producto: ").strip())
nueva_cantidad = int(input("Ingrese la cantidad del nuevo producto: ").strip())
nuevo_producto = {
    "nombre": nuevo_nombre,
    "precio": nuevo_precio,
    "cantidad": nueva_cantidad
}
productos.append(nuevo_producto)
with open("07 Manejo de Archivos/productos.txt", "w",encoding="utf-8") as archivo:
    for producto in productos:
        archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
print("Archivo productos.txt actualizado con éxito.")
print("\nProductos actualizados:")
for producto in productos:
    print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
    