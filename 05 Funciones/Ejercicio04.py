# 4. Crear dos funciones: 
# calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados
import math
def calcular_area_circulo(radio: float)-> float:
    formula_area=math.pi*(radio**2)
    return formula_area

radio=float(input("Ingrese el radio del circulo: "))
area_circulo=calcular_area_circulo(radio)
print(f"El Area del circulo es: {area_circulo:.2f}")
print("-----------------------------------")

def calcular_perimetro_circulo(radio: float)->float:
    formula_perimetro= 2*math.pi*radio
    return formula_perimetro

perimetro=calcular_perimetro_circulo(radio)
print(f"El Perimetro del circulo es: {perimetro:.2f}")
print("-----------------------------------")