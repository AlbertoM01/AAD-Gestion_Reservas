"""
Ejercicio3.py - Manejo de errores
-----------------------------------

1. Crear un archivo de datos maestro corrupto
2. Leer, clasificar y registrar errores
3. Verificar e informar errores
"""

import os
from datetime import datetime

fichero_maestro = "src/Parte3/reservas_maestro_con_errores.txt"
log_errores = "src/Parte3/registro_errores.log"

class Reserva:
    def __init__(self, asiento, nombre, clase, destino):
        self.asiento = asiento.strip()
        self.nombre = nombre.strip()
        self.clase = clase.strip()
        self.destino = destino.strip()

    def __str__(self):
        return f"{self.asiento}, {self.nombre}, {self.clase}, {self.destino}"


"""Clase encargada de registrar los errores."""
class LoggerErrores:
    def __init__(self, log_file=log_errores):
        self.log_file = log_file
        if os.path.exists(self.log_file):  # Eliminar log anterior si existe
            os.remove(self.log_file)

    def registrar(self, linea, descripcion):
        with open(self.log_file, "a", encoding="utf-8") as log:
            log.write(
                f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, {linea.strip()}, {descripcion}\n"
            )


class GestorReservas:
    def __init__(self, fichero_maestro, logger):
        self.fichero_maestro = fichero_maestro
        self.log_errores = log_errores
        self.logger = logger
        self.reservas_validas = {}

    def validar_linea(self, linea):
        """Valida una línea del fichero."""
        if not linea.strip():
            self.logger.registrar(linea, "Linea vacía")
            return None

        campos = [c.strip() for c in linea.split(",")]
        if len(campos) != 4:
            self.logger.registrar(linea, "Número incorrecto de campos")
            return None

        asiento, nombre, clase, destino = campos
        if not asiento or not nombre or not clase or not destino:
            self.logger.registrar(linea, "Faltan datos obligatorios")
            return None

        return Reserva(asiento, nombre, clase, destino)

    def crear_fichero_maestro(self):
        """Crea el archivo reservas_maestro.txt con las reservas de ejemplo."""
        with open(self.fichero_maestro, "w", encoding="utf-8") as f:
            print(f"✅ Archivo maestro '{self.fichero_maestro}' creado.")
    
    def crear_fichero_log(self):
        """Crea el archivo .txt con las reservas de ejemplo."""
        with open(self.log_errores, "w", encoding="utf-8") as f:
            print(f"✅ Archivo de log '{self.log_errores}' creado.")

    def procesar(self):
        """Lee el fichero maestro y clasifica reservas válidas y errores."""
        with open(self.fichero_maestro, "r", encoding="utf-8") as f:
            for linea in f:
                reserva = self.validar_linea(linea)
                if reserva:
                    self.guardar_reserva(reserva)

    def guardar_reserva(self, reserva):
        """Guarda una reserva válida en el fichero de su destino."""
        fichero_destino = f"reservas_{reserva.destino}.txt"
        with open(fichero_destino, "a", encoding="utf-8") as fd:
            fd.write(str(reserva) + "\n")

        # Contabilizar reservas por destino
        self.reservas_validas[reserva.destino] = (
            self.reservas_validas.get(reserva.destino, 0) + 1
        )

    def resumen(self):
        """Muestra un resumen de los ficheros creados y los errores."""
        print("Resumen de ficheros generados:")
        for destino, count in self.reservas_validas.items():
            print(f" - reservas_{destino}.txt: {count} reservas válidas")

        print("\n Contenido de registro_errores.log:")
        if os.path.exists(log_errores):
            with open(log_errores, "r", encoding="utf-8") as log:
                print(log.read())
        else:
            print("No se han encontrado errores ✅")

def ejecutar_gestor():
    logger = LoggerErrores()
    gestor = GestorReservas(fichero_maestro, logger)
    gestor.crear_fichero_maestro()
    gestor.crear_fichero_log()
    gestor.procesar()
    gestor.resumen()
    return gestor

if __name__ == "__main__":
    ejecutar_gestor()
