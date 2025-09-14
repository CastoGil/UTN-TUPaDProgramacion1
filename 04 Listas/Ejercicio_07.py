# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
# semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.

dias=["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]

temperaturas_semana = [
    [15, 25],  # Lunes
    [17, 28],  # Martes
    [14, 22],  # Miércoles
    [16, 30],  # Jueves
    [18, 27],  # Viernes
    [19, 29],  # Sábado
    [13, 24]   # Domingo
]

temperatura_minima=0
temperatura_maxima=0
mayor_amplitud=0
dia_mayor_amplitud=""

for i in range(len(temperaturas_semana)):
    temperatura_minima += temperaturas_semana[i][0]
    temperatura_maxima += temperaturas_semana[i][1]
    
    amplitud = temperaturas_semana[i][1] - temperaturas_semana[i][0]
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = dias[i]
        
promedio_minima = temperatura_minima / len(temperaturas_semana)
promedio_maxima = temperatura_maxima / len(temperaturas_semana)
print(f"Promedio de temperaturas mínimas: {promedio_minima:.2f}°C")
print(f"Promedio de temperaturas máximas: {promedio_maxima:.2f}°C")
print(f"Día con mayor amplitud térmica: {dia_mayor_amplitud} con una amplitud de {mayor_amplitud}°C")