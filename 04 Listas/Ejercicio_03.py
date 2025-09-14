# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

import random

numeros=[]
for _ in range(15):
    numeros.append(random.randint(1,100))
    
print(f"Lista de números generados: {sorted(numeros)}")

numeros_pares=[]
numeros_impares=[]

for num in numeros:
    if num % 2==0:
        numeros_pares.append(num)
    else:
        numeros_impares.append(num)
        

numeros_pares = sorted(numeros_pares)
numeros_impares = sorted(numeros_impares)

print("\nNúmeros impares:")
for n in numeros_impares:
    print(n)
print(f"Cantidad de numeros en la lista de impares: {len(numeros_impares)}")

print("\nNúmeros pares:")
for n in numeros_pares:
    print(n)
print(f"Cantidad de números en la lista de pares: {len(numeros_pares)}")