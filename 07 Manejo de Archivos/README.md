# 07 — Manejo de Archivos en Python

**Cátedra:** Programación 1 — TUP (UTN)  
**Unidad:** Lectura, escritura y persistencia de datos en archivos de texto.

---

## 🌟 Objetivos

* Comprender y aplicar el uso de **archivos de texto en Python**.
* Manipular datos mediante **lectura, escritura y actualización** de información persistente.
* Utilizar estructuras como **listas** y **diccionarios** para almacenar productos en memoria.
* Aplicar buenas prácticas: `with open()`, control de modos (`r`, `w`, `a`) y validaciones básicas.

---

## 📚 Índice de ejercicios

> Convención: nombres con **cero a la izquierda** para mantener orden en GitHub (`Ejercicio01.py` … `Ejercicio06.py`).

| Archivo | Descripción | Ejecutar |
|----------|--------------|-----------|
| [Ejercicio01.py](./Ejercicio01.py) | Crea el archivo `productos.txt` con tres productos iniciales. | `python Ejercicio01.py` |
| [Ejercicio02.py](./Ejercicio02.py) | Lee el archivo y muestra los productos con formato. | `python Ejercicio02.py` |
| [Ejercicio03.py](./Ejercicio03.py) | Permite **agregar un nuevo producto** desde teclado sin borrar los existentes. | `python Ejercicio03.py` |
| [Ejercicio04.py](./Ejercicio04.py) | Carga los productos en una **lista de diccionarios** con claves `nombre`, `precio`, `cantidad`. | `python Ejercicio04.py` |
| [Ejercicio05.py](./Ejercicio05.py) | Permite **buscar un producto por nombre** e informar si existe o no. | `python Ejercicio05.py` |
| [Ejercicio06.py](./Ejercicio06.py) | Integra lectura, agregado y guardado: sobrescribe el archivo con los productos actualizados. | `python Ejercicio06.py` |


## ▶️ Cómo ejecutar
1. Verificá que tenés **Python 3.x** (`python --version`).
2. Desde esta carpeta, ejecutá el script deseado:
   ```bash
   python Ejercicio01.py
