"""
Main.py
-------
Controlador principal que utiliza GestorReservas para crear y clasificar reservas.
"""

from Parte2.Ejercicio2 import GestorReservas
from Parte3.Ejercicio3 import ejecutar_gestor

def main():
    print("=== PARTE 2 ===")
    print("=== Sistema de Gestión de Reservas ===")
    gestor = GestorReservas()
    # Crear archivo maestro de reservas
    gestor.crear_archivo_maestro()
    # Clasificar reservas por destino y mostrar resumen
    gestor.clasificar_por_destino()
    
    print("=== PARTE 3 ===")
    print("=== Sistema de Registro de Errores ===")
    ejecutar_gestor()

if __name__ == "__main__":
    main()
    