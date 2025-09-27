"""
Ejercicio2.py
--------------
Clase GestorReservas que permite:
1. Crear el archivo maestro de reservas.
2. Clasificar reservas por destino y mostrar un resumen por consola.
"""

import os

class GestorReservas:
    def __init__(self, archivo_maestro="reservas_maestro.txt", ruta="./src/Parte2/"):
        self.archivo_maestro = ruta+archivo_maestro
        self.reservas = [
            "12A, Juan Pérez, Economy, Madrid",
            "14B, María López, Business, París",
            "21C, Carlos García, Economy, Madrid",
            "05D, Ana Sánchez, Business, Londres",
            "19E, Luis Gómez, Economy, París",
            "08F, Sofía Vargas, Economy, Londres"
        ]

    def crear_archivo_maestro(self):
        """Crea el archivo reservas_maestro.txt con las reservas de ejemplo."""
        with open(self.archivo_maestro, "w", encoding="utf-8") as f:
            for reserva in self.reservas:
                f.write(reserva + "\n")
        print(f"✅ Archivo maestro '{self.archivo_maestro}' creado.")

    def clasificar_por_destino(self):
        """Lee el archivo maestro y crea archivos por destino con las reservas correspondientes."""
        if not os.path.exists(self.archivo_maestro):
            print(f"❌ Error: El archivo '{self.archivo_maestro}' no existe.")
            return

        archivos_destino = {}  # Diccionario para contar reservas por archivo

        with open(self.archivo_maestro, "r", encoding="utf-8") as f:
            for linea in f:
                datos = linea.strip().split(", ")
                if len(datos) != 4:
                    print(f"⚠️ Línea ignorada por formato incorrecto: {linea}")
                    continue

                asiento, nombre, clase, destino = datos
                archivo_destino = f"./src/Parte2/reservas_{destino.lower()}.txt"

                # Crear o abrir archivo de destino
                with open(archivo_destino, "a", encoding="utf-8") as fd:
                    fd.write(linea)

                # Contador de reservas por archivo
                if archivo_destino not in archivos_destino:
                    archivos_destino[archivo_destino] = 0
                archivos_destino[archivo_destino] += 1

        # Mostrar resumen final por consola
        print("\n📂 Resumen de archivos por destino:")
        for archivo, count in archivos_destino.items():
            print(f"{archivo}: {count} reservas")