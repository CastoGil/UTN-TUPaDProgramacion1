#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.
num=int(input("ingrese un numero entero: "))
suma=0
while num!=0:
    suma=suma+num
    num=int(input("ingrese un numero entero , si el numero es 0 termina el programa:"))
   
print(f"la suma total es: {suma}")