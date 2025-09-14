# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.

ventas = [
    [150, 200, 250, 300, 350, 400, 450],
    [100, 150, 200, 250, 23300, 350, 400],
    [200, 250, 300, 350, 400, 450,  500],
    [300, 350, 400, 450, 15500, 550,  600]
]   
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]   
productos = ["Producto A", "Producto B", "Producto C", "Producto D"]
num_productos = len(ventas)
num_dias = len(ventas[0])

# Total vendido por cada producto
totales_productos = []
for i in range(num_productos):
    total_producto=0
    for j in range(num_dias):
        total_producto += ventas[i][j]
    totales_productos.append(total_producto)
    print(f"Total vendido del {productos[i]}: {total_producto}")
    
# Día con mayores ventas totales
mayor_venta_dia = 0
dia_mayor_venta = ""
for j in range(num_dias):
    total_dia = 0
    for i in range(num_productos):
        total_dia += ventas[i][j]
        
    if total_dia > mayor_venta_dia:
        mayor_venta_dia = total_dia
        dia_mayor_venta = dias[j]
print(f"Día con mayores ventas totales: {dia_mayor_venta} con {mayor_venta_dia} ventas.")

# Producto más vendido en la semana
producto_mas_vendido = productos[0]
mayor_venta_producto = totales_productos[0]
for i in range(num_productos):
    if totales_productos[i] > mayor_venta_producto:
        mayor_venta_producto = totales_productos[i]
        producto_mas_vendido = productos[i]
print(f"Producto más vendido en la semana: {producto_mas_vendido} con {mayor_venta_producto} ventas.")


