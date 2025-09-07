#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).
suma=0
cantidad=5
for i in range (0,cantidad):
    num=int(input("ingrese un numero entero: "))
    suma+=num
    
media= suma/cantidad
print(f"la media es : {media}")