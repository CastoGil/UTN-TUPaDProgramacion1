# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso:float,altura:float)->float:
    if peso <= 0 or altura <= 0:
        print("Los valores deben ser mayores que 0")
        return None
    else:
        imc= peso/(altura**2)
        return imc

peso=float(input("Ingrese el peso en kg(kilogramos): "))
altura=float(input("Ingrese la altura en m(metros): "))

resultado_imc=calcular_imc(peso,altura)

if resultado_imc is not None:
    print("\n-- Resultado --")
    print(f"El índice de masa corporal es: {resultado_imc:.2f} kg/m²")