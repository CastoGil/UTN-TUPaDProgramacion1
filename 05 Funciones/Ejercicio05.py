# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
def segundos_a_horas(segundos:float)->float:
    formula= (segundos/3600)
    return formula


ingresar_segundos=float(input("Ingrese los segundos: "))
horas=segundos_a_horas(ingresar_segundos)
print(f"La cantidad de horas es: {horas:.2f}")
