# 4) Dada una lista con valores repetidos: datos=[1,3,5,3,7,1,9,5,3]
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.
datos=[1,3,5,3,7,1,9,5,3]
print(f"Lista de datos: {datos}")
lista_nueva=[]

for n in datos:
    if n not in lista_nueva:
        lista_nueva.append(n)
    
print(f"Lista de datos nueva : {lista_nueva}")