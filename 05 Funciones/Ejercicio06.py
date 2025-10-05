# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.
def tabla_multiplicar(numero:int)-> None:
    if numero <= 0:
        print("Ingrese un numero mayor que 0")
    else:
        print(f"La tabla de multiplicar del numero {numero}: ")
        for i in range(1,11):
            calculo=numero*i
            print(f"{numero} x {i} = {calculo}")
            
        
    
ingresar_numero=int(input("Ingrese un numero para mostrar su tabla de multiplicar: "))
tabla_multiplicar(ingresar_numero)
