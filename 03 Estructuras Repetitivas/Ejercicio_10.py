#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

n=int(input("Ingrese un numero: "))
invertir_num=0
num=abs(n)
while num>0:
    digito= num % 10 
    invertir_num= invertir_num*10 + digito
    num= num //10

if n<0: 
    invertir_num=-invertir_num
print(f"el numero invertido es {invertir_num}")