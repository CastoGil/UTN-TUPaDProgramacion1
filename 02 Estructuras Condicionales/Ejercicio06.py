#Escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Definir la lista numeros_aleatorios de la siguiente forma:
#import random
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
#forma aleatoria.
# ===============================================================
import random
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print(f"Números aleatorios: {numeros_aleatorios}")

mode = mode(numeros_aleatorios)
median = median(numeros_aleatorios)
mean = mean(numeros_aleatorios)
print(f"Moda: {mode}, Mediana: {median}, Media: {mean}")

if mean > median and mean > mode:
    print("Sesgo positivo")
elif mean < median and mean < mode:
    print("Sesgo negativo")
else:
    print("No hay sesgo")
