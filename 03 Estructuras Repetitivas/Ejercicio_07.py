#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.
num=int(input("ingrese un numero entero positivo: "))
suma=0

if num <0:
    print("ingrese un numero mayor a 0")
else:    
    for i in range(0,num+1):
        suma+=i
    print(f"la suma de todos los numeros comprendidos entre 0 y {num} es: {suma}")
    
