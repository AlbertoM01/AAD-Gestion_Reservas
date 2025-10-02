"""
Parte 1 - Gestión básica de reservas en archivo de texto.

Este módulo simula el sistema de reservas de un vuelo:
1. Crea un archivo de texto con las reservas.
2. Lee las reservas desde el archivo.
3. Muestra la información de manera legible.
4. Cuenta el total de reservas y los pasajeros en clase Business.
"""

# Clase que representa una reserva individual
class Reserva:
    def __init__(self, asiento, pasajero, clase):
        self.asiento = asiento
        self.pasajero = pasajero
        self.clase = clase

    def __str__(self):
        return f"Asiento: {self.asiento}, Pasajero: {self.pasajero}, Clase: {self.clase}"
class GestorReserva:
    """
    Lee el archivo 'reservas.txt' y procesa la información:
    - Imprime cada reserva en formato legible.
    - Muestra el número total de reservas.
    - Muestra cuántos pasajeros viajan en clase Business.
    """
    def __init__(self, archivo="./src/Parte1/reservas.txt"):
        self.archivo = archivo

    def guardar_reservas(self, reservas):
        """Escribe reservas en el archivo"""
        with open(self.archivo, "w", encoding="utf-8") as f:
            for reserva in reservas:
                f.write(f"{reserva.asiento}, {reserva.pasajero}, {reserva.clase}\n")

    # Imprimir reservas de manera legible
    def leer_reservas(self):
        """Lee reservas desde el archivo"""
        reservas = []
        with open(self.archivo, "r", encoding="utf-8") as f:
            for linea in f:
                # Dividimos la línea en asiento, nombre y clase
                asiento, pasajero, clase = linea.strip().split(", ")
                reservas.append(Reserva(asiento, pasajero, clase))
        return reservas

    def procesar_reservas(self):
        """Muestra información procesada"""
        reservas = self.leer_reservas()

        print("📌 Listado de reservas:")
        for reserva in reservas:
            print(reserva)

        total = len(reservas)
        business = sum(1 for r in reservas if r.clase.lower() == "business")

        print("\n📊 Resultados:")
        print(f"Total de reservas: {total}")
        print(f"Pasajeros en clase Business: {business}")
