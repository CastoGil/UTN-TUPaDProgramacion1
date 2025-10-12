# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.
# Ejemplo: original={"Argentina":"Buenos Aires", "Chile":"Santiago"}, invertido={"Buenos Aires":"Argentina", "Santiago":"Chile"}
paises={
     "Argentina": "Buenos Aires",
     "Chile": "Santiago",
     "Uruguay": "Montevideo",
     "Brasil": "Brasilia",
     "Paraguay": "Asunción"
}
invertido={}
for clave,valor in paises.items():
    invertido[valor]=clave
print(f"Diccionario original: {paises}")
print("--------------------------------------------")
print(f"Diccionario invertido : {invertido}")