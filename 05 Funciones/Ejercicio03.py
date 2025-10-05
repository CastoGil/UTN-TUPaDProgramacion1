# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre: str, apellido: str, edad: int, residencia: str)-> str:
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

nombre=input("Ingrese su nombre: ").strip().capitalize()
apellido=input("Ingrese su apellido: ").strip().capitalize()
edad=int(input("Ingrese su edad: "))
residencia=input("Ingrese su lugar de residencia: ").strip().capitalize()

informacion=informacion_personal(nombre,apellido,edad,residencia)
print(informacion)