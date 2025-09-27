"""
Main.py
-------
Controlador principal que utiliza GestorReservas para crear y clasificar reservas.
"""

from Parte2.Ejercicio2 import GestorReservas

def main():
    gestor = GestorReservas()

    # Crear archivo maestro de reservas
    gestor.crear_archivo_maestro()

    # Clasificar reservas por destino y mostrar resumen
    gestor.clasificar_por_destino()

if __name__ == "__main__":
    main()