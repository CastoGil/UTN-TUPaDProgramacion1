# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.
productos = []
with open("07 Manejo de Archivos/productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)
        
nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip()
encontrado = False

for producto in productos:
    if producto["nombre"].lower() == nombre_buscar.lower():
        print(f"Producto encontrado: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
        encontrado = True
        break
if not encontrado:
    print("Error: Producto no encontrado.")
    
