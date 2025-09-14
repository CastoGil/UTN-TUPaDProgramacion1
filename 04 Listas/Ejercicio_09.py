# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.

tablero = []
for _ in range(3):
   fila=[]
   for _ in range(3):
        fila.append("-")
   tablero.append(fila)

turno = 0
jugador_actual = "X"

while turno < 9:
    print("Tablero actual:")

    for f in range(3):
        print(tablero[f][0], tablero[f][1], tablero[f][2])
    print(f"Turno del jugador {jugador_actual}")
    
    fila = int(input("Ingrese la fila (0, 1, 2): "))
    columna = int(input("Ingrese la columna (0, 1, 2): "))
    
    if fila < 0 or fila > 2 or columna < 0 or columna > 2:
        print("Posición inválida. Intente de nuevo.")
        continue
    
    if tablero[fila][columna] != "-":
        print("Casilla ya ocupada. Intente de nuevo.")
        continue
    
    tablero[fila][columna] = jugador_actual
    turno += 1
    jugador_actual = "O" if jugador_actual == "X" else "X"
    
print("Tablero final:")


for f in range(3):
    print(tablero[f][0], tablero[f][1], tablero[f][2])
    
            

    