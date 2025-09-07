#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

#importamos random ya que es la manera de que el programa nos de un numero aleatorio
import random

print("Vamos a jugar!! Adivina el número entre 0 y 9")
num_aleatorio = random.randint(0, 9)
intentos = 0
while True:
    num=int(input("ingrese un numero (0-9): "))
    if num <0 or num>9:
        print("Numero fuera del rango (0-9), intentalo de nuevo")
        continue
    intentos +=1
    if num==num_aleatorio:
        print(f"¡Acertaste! el numero de intentos fue: {intentos}, el numero aleatorio era: {num_aleatorio}")
        break
    else:
        print("No acertaste, sigue intentandolo!")