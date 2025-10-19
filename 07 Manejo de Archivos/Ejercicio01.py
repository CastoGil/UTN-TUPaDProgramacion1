# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado
# productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad
with open("07 Manejo de Archivos/productos.txt", "w",encoding="utf-8") as archivo:
    archivo.write("Manzana,100,100\n")
    archivo.write("Banana,200,150\n")
    archivo.write("Naranja,300,80\n")
print("productos.txt creado con éxito.")