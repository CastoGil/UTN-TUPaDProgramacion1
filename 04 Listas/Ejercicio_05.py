# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

estudiantes=["Mario", "Pedro", "Juan" , "Carlos", "Maria", "Matias" ,"José", "Diego"]
print(f"Lista de estudiantes: {estudiantes}")
pregunta=input("Desea agregar o eliminar a un estudiante (A:agregar / E:eliminar)? : ").upper()
if pregunta=="A" :
    agregar_estudiante=input("Escribe el nombre del nuevo estudiante: ").capitalize()
    estudiantes.append(agregar_estudiante)
    print("\nLista actualizada de estudiantes:")
    for e in estudiantes:
        print(e)
elif pregunta == "E":
    eliminar_estudiante = input("Escribe el nombre del estudiante que deseas eliminar: ").capitalize()
    if eliminar_estudiante in estudiantes:
        estudiantes.remove(eliminar_estudiante)
        print("\nLista actualizada de estudiantes:")
        for e in estudiantes:
            print(e)
    else:
        print(f"⚠️  El estudiante '{eliminar_estudiante}' no se encuentra en la lista.")
 
else:
    print("⚠️  Ingresa una opción válida (A o E).")