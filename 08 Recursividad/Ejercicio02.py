# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

numero = int(input("Introduce la posición hasta la cual deseas ver la serie de Fibonacci: "))
for i in range(numero):
    print(f"Fibonacci en la posición {i} es {fibonacci(i)}")
    