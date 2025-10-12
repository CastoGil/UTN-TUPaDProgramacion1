# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
# Ejemplo: contactos= {"Juan": "123456", "Ana":"987654"} 
# Consultar: "Juan" ->muestra "123456"

telefonos={}
for i in range(5):
    nombre=input("Ingrese su nombre: ").strip().capitalize()
    telefono=input("Ingrese su numero de telefono: ").strip()
    telefonos[nombre]=telefono
    
print(f"\nRegistro de telefonos: {telefonos}")
solicitar_nombre=input("\nIngrese el nombre del contacto que desea buscar: ").strip().capitalize()

if solicitar_nombre in telefonos:
    nombre_buscado=solicitar_nombre
    telefono_buscado=telefonos[solicitar_nombre]
    print(f"El numero de celular de {nombre_buscado} es: {telefono_buscado}")
else:
    print("El nombre ingresado no existe ")
    