# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.
# Ejemplo: Entrada -> "hola mundo hola"
# Salida: Palabras_unicas: {'hola', 'mundo'} , Recuento:{'hola':2, 'mundo':1}

solicitar_frase=input("Ingrese una frase: ").lower().split()


palabras_unicas= set(solicitar_frase)
print(f"Palabras unicas: {palabras_unicas}")

diccionario={}
for palabra in solicitar_frase:
    if palabra in diccionario:
        diccionario[palabra]+=1
    else: 
        diccionario[palabra]=1

print(f"\nCantidad de veces que aparece cada palabra: {diccionario}")
        