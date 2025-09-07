#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.
num1=int(input("Ingrese el primer numero entero:"))
num2=int(input("Ingrese el segundo numero entero:"))
suma=0
if num1==num2:
    print("La suma de los números estrictamente entre ellos es: 0")
else:    
    if num1>num2:
        valor2=num1
        valor1=num2
    else: 
        valor2=num2
        valor1=num1
        
    for i in range (valor1+1, valor2):
        suma =suma + i
    print(f"la suma de todos los numero entero es : {suma}")
    