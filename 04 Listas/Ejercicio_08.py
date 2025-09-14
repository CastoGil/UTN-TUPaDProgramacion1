# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

materias=["Matemáticas", "Historia", "Ciencias"]
estudiantes=["Maria", "Vanessa", "Juan", "Pedro", "Mario"]

notas = [
    [7.5, 8.0, 6.5],  
    [9.0, 5.5, 7.0], 
    [8.5, 6.0, 9.5], 
    [7.8, 8.2, 6.9],  
    [6.5, 7.5, 8.0]   
]
print("Notas de cada estudiante:")
for i in range(len(estudiantes)):
    print(f"\n {estudiantes[i]} saco las siguientes notas:")
    for j in range(len(materias)):
        print(f" {materias[j]}: {notas[i][j]}")
    promedio_estudiante = sum(notas[i]) / len(materias)
    print(f"---Promedio de {estudiantes[i]}: {promedio_estudiante:.2f}")

print("\nPromedio de cada materia:")

num_estudiantes = len(notas)
num_materias = len(notas[0])

for j in range (num_materias):
    suma=0
    for i in range(num_estudiantes):
        suma += notas[i][j]
    promedio_materia = suma / num_estudiantes
    print(f"---Promedio de {materias[j]}: {promedio_materia:.2f}")