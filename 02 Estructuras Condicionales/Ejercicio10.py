# 10) — Estaciones del año según fecha y hemisferio
# Enunciado:
# Utilizando la información de la siguiente tabla (rangos INCLUIDOS):
# ===============================================================
# Periodo del año                 | Hemisferio norte | Hemisferio sur
# 21 de diciembre – 20 de marzo   | Invierno         | Verano
# 21 de marzo – 20 de junio       | Primavera        | Otoño
# 21 de junio – 20 de septiembre  | Verano           | Invierno
# 21 de septiembre – 20 de diciembre | Otoño         | Primavera
#
# Escribir un programa que pregunte al usuario en cuál hemisferio se
# encuentra (N/S), qué mes del año es y qué día es. El programa deberá
# utilizar esa información para imprimir por pantalla si el usuario se
# encuentra en otoño, invierno, primavera o verano.
# ===============================================================

hemisferio = input("Ingrese su hemisferio (N/S): ").strip().upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

if (mes == 12 and dia >= 21) or (mes in (1, 2)) or (mes == 3 and dia <= 20):
    hemisferio_Norte_Estacion = "Invierno"
elif (mes == 3 and dia >= 21) or (mes in (4, 5)) or (mes == 6 and dia <= 20):
    hemisferio_Norte_Estacion = "Primavera"
elif (mes == 6 and dia >= 21) or (mes in (7, 8)) or (mes == 9 and dia <= 20):
    hemisferio_Norte_Estacion = "Verano"
else:
    hemisferio_Norte_Estacion= "Otoño"

if hemisferio == "N":
    print(f"En el hemisferio norte es {hemisferio_Norte_Estacion}")
elif hemisferio == "S":
    if hemisferio_Norte_Estacion == "Invierno":
        hemisferio_Sur_Estacion = "Verano"
    elif hemisferio_Norte_Estacion == "Primavera":
        hemisferio_Sur_Estacion = "Otoño"
    elif hemisferio_Norte_Estacion == "Verano":
        hemisferio_Sur_Estacion = "Invierno"
    else:
        hemisferio_Sur_Estacion = "Primavera"
    print(f"En el hemisferio sur es {hemisferio_Sur_Estacion}")


