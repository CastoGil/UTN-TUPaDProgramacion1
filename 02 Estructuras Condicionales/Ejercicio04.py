#Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.
# ===============================================================

edad_usuario= int(input("Ingrese su edad: "))
if edad_usuario < 12:
    print("Usted es un niño/a")
elif 12 <= edad_usuario < 18:
    print("Usted es un adolescente")
elif 18 <= edad_usuario < 30:
    print("Usted es un adulto/a joven")
else:
    print("Usted es un adulto/a")
    