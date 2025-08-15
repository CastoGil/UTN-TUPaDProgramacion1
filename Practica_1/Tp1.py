# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

nombre = input(" Ingrese su nombre: ")
print(f"Hola {nombre}")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

nombre_usuario= input(" Ingrese su nombre: ")
apellido_usuario= input (" Ingrese su apellido: ")
edad_usuario = int(input (" Ingrese su edad: "))
residencia_usuario = input(" Ingrese su residencia: ")
print(f"Soy {nombre_usuario} {apellido_usuario}, tengo {edad_usuario} y vivo en {residencia_usuario}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.
import math
radio= float(input ("ingrese el radio del circulo : "))
area= math.pi*(radio**2)
perimetro= 2 * math.pi * radio
print(f"El area del circulo es : {area:.2f} y su perimetro : {perimetro:.2f}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

cantidad_sg= int(input(" ingrese los segundos :"))
equivalente_horas= (cantidad_sg/3600)
print(f"la cantidad de horas aproximadamente son : {equivalente_horas:.2f}")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

numero_tabla= int(input("ingrese un numero: "))
print (f"La tabla de multiplicar de {numero_tabla} ")
for i in range(1,11):
    tabla_multiplicar= numero_tabla * i
    print(f"{numero_tabla} * {i} = {tabla_multiplicar}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero1=int(input("ingrese el primer numero entero distinto de 0 : "))
numero2=int(input("ingrese el segundo numero entero distinto de 0 : "))
if numero1 !=0 and numero2 !=0:
    suma= numero1+numero2
    multiplicacion= numero1*numero2
    division= numero1/numero2
    resta= numero1-numero2
    print(f" la suma de los dos numeros es {suma}")
    print(f" la resta de los dos numeros es {resta}")
    print(f" la multiplicacion de los dos numeros es {multiplicacion}")
    print(f" la division de los dos numeros es {division:.2f}")
else:
    print("Error no tiene que ser cero")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo:         𝐼𝑀𝐶 =𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔
#               (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)**2

altura=float(input("ingrese su altura en metros: "))
peso=float(input("ingrese su peso en kg: "))
masa_corporal= peso /(altura**2)
print (f"Su índice de masa corporal (IMC) es : {masa_corporal:.2f}  kg/m²")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = (9/5)*𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

temperatura_Celsius= float(input("ingrese la temperatura en grados celsius°: "))
temperatura_fahrenheit= ((9/5)*temperatura_Celsius)+ 32
print(f"la temperatura en grados fahrenheit es equivalente a : {temperatura_fahrenheit:.2f}°F")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.
numero_1= int(input("ingrese el primer numero: "))
numero_2= int(input("ingrese el segundo numero: "))
numero_3= int(input("ingrese el tercer numero: "))
promedio= (numero_1+numero_2+numero_3)/3
print(f"el promedio es {promedio:.2f}")

