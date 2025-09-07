#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).
cont_par=0
cont_impar=0
cont_positivo=0
cont_negativo=0
for i in range(0,100):
    num=int(input("ingresa un numero entero: "))
    if num % 2==0:
        cont_par+=1
    else:
        cont_impar+=1
    
    if num>=0 :
        cont_positivo+=1
    else:
        cont_negativo+=1
    
print(f"cantidad de numeros pares:{cont_par}")
print(f"cantidad de numeros impares:{cont_impar}")     
print(f"cantidad de numeros positivos:{cont_positivo}")
print(f"cantidad de numeros negativos:{cont_negativo}")