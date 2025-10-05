# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.
def operaciones_basicas(a:float,b:float)->tuple:
    suma= a+b
    resta=a-b
    multiplicacion=a*b
    if b==0 :
        division="No se puede dividir por cero"
    else:
        division= a/b
    return (suma,resta,multiplicacion,division)

num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))
suma,resta,multiplicacion,division=operaciones_basicas(num1,num2)

print("\n--- Resultados ---")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")