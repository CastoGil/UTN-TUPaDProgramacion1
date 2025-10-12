# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.
# Ejemplo: alumnos={ "Sofia:"(10,9,8),"Luis:" (6,7,7)}
alumnos={}

for alumno in range(3):
    nombre_alumno=input(f"Ingrese el nombre del alumno {alumno+1}: ")
    
    notas=[]
    
    for nota in range(3):
        calificacion=float(input(f"Ingrese la nota {nota+1}: "))
        notas.append(calificacion)
    
    alumnos[nombre_alumno]=tuple(notas)
    
print("\nRegistro de alumnos y sus notas:")
print(alumnos)

print("\nPromedios:")
 
for nombre,notas in alumnos.items():
    promedio= sum(notas)/len(notas)
    print(f"{nombre}: promedio {promedio:.2f}")