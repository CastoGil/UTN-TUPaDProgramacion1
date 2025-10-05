# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.
def celsius_a_fahrenheit(celsius: float)->float:
    calculo_fahrenheit= (celsius*9/5)+32
    return calculo_fahrenheit

temperatura_celsius=float(input("Ingrese la temperatura en grados celsius °C: "))
fahrenheit=celsius_a_fahrenheit(temperatura_celsius)
print(f"La temperatura en grados Fahrenheit es :{fahrenheit:.2f} °F ")