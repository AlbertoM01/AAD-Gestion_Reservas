"""
Main.py
-------
Controlador principal que utiliza GestorReservas para crear y clasificar reservas.
"""
from Parte1.Ejercicio1 import Reserva
from Parte1.Ejercicio1 import GestorReserva
from Parte2.Ejercicio2 import GestorReservas
from Parte3.Ejercicio3 import ejecutar_gestor

def main():
    print("=== PARTE 1 ===")
    print("=== Sistema de Gestión de Reservas ===")
    reservas = [
        Reserva("12A", "Juan Pérez", "Economy"),
        Reserva("14B", "María López", "Business"),
        Reserva("21C", "Carlos García", "Economy")
    ]

    gestor = GestorReserva("./src/Parte1/reservas.txt")

    # Guardar en archivo
    gestor.guardar_reservas(reservas)

    # Procesar y mostrar resultados
    gestor.procesar_reservas()

    print("\n=== PARTE 2 ===")
    print("=== Sistema de Gestión de Reservas ===")
    gestor = GestorReservas()
    # Crear archivo maestro de reservas
    gestor.crear_archivo_maestro()
    # Clasificar reservas por destino y mostrar resumen
    gestor.clasificar_por_destino()
    
    print("\n=== PARTE 3 ===")
    print("=== Sistema de Registro de Errores ===")
    ejecutar_gestor()

if __name__ == "__main__":
    main()
    