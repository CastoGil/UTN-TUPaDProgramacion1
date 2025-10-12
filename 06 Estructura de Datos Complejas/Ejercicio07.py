# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial_1={7,10,6,8,5,2} #Cada número del conjunto representa a un alumno, no una calificación.
parcial_2={8,9,10}

ambos_parciales=parcial_1&parcial_2
aprobaron_uno=parcial_1 ^ parcial_2
al_menos_uno=parcial_1|parcial_2

print(f"Ambos parciales: {ambos_parciales} ")
print(f"Solo uno: {aprobaron_uno} ")
print(f"Al menos uno: {al_menos_uno}")