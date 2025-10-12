# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Ejemplo: agenda= {("lunes", "10:00"): "Reunion", ("martes", "15:00"): "Clase de ingles"}
# Permití consultar qué actividad hay en cierto día y hora.
agenda = {
    ("lunes", "10:00"): "Reunión de trabajo",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:00"): "Gimnasio",
    ("viernes", "20:00"): "Cena con amigos"
}
consultar_dia= input("Ingresa el dia a consultar: ").strip().lower()
consultar_hora=input("Ingresa la hora formato(hh:mm): ").strip()

if (consultar_dia, consultar_hora) in agenda:
    actividad=agenda[(consultar_dia,consultar_hora)]
    print(f"Actividad programada para el dia {consultar_dia}: {actividad}")
else:
    print(f"No hay ninguna actividad programada para el dia {consultar_dia}")
    
    