#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

num= int(input("ingrese un número entero:" ))
n = abs(num)
if n == 0:
    digitos = 1
else:
    digitos = 0
    while n != 0:
        n //= 10
        digitos += 1
print(f"La cantidad de dígitos es:{digitos}")
    
