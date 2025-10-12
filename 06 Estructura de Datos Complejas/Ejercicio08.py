# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

stock_productos={'Leche':10,'Harina':20,'Manteca':30,'Huevos':50 }

consulta=input("Ingrese el producto a consultar: ").strip().capitalize()
if consulta in stock_productos:
    print(f"El producto tiene {stock_productos[consulta]}")
    agregar_unidades=int(input("Ingrese las unidades agregar: "))
    stock_productos[consulta]+=agregar_unidades
else:
    print("El producto ingresado no existe")
    nuevo_stock=int(input("Ingrese las unidades del nuevo producto: "))
    stock_productos[consulta]= nuevo_stock

print("Stock actualizado: ")
print(stock_productos)
    
