#1) Crear una lista con las notas de 10 estudiantes.
#• Mostrar la lista completa.
#• Calcular y mostrar el promedio.
#• Indicar la nota más alta y la más baja.


notas = [7.5, 8.0, 6.5, 9.0, 5.5, 7.0, 8.5, 6.0, 9.5, 7.8]
print(f"Lista de notas: {notas}")
promedio = sum(notas) / len(notas)
print(f"Promedio de notas: {promedio:.2f}")
nota_mas_alta = max(notas)
nota_mas_baja = min(notas)
print(f"Nota más alta: {nota_mas_alta}")
