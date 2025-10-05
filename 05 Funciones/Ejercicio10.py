# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.
def calcular_promedio(a:float,b:float,c:float)->float:
    promedio= (a+b+c)/3
    return promedio
num1=float(input("Ingresar el primer numero : "))
num2=float(input("Ingresar el segundo numero : "))
num3=float(input("Ingresar el tercer numero : "))

resultado=calcular_promedio(num1,num2,num3)
print(f"El promedio es : {resultado:.2f}")
