# almacen_json.py
#
# Clase AlmacenJson para persistencia en archivos JSON.
#
# ===============================
# CUMPLIMIENTO DE REQUISITOS
# ===============================
#
# Req 2:
# - Implementa persistencia en archivos para Hotels, Customers y Reservations
#   mediante los metodos cargar() y guardar().
#
# Req 5:
# - Maneja archivo invalido o datos corruptos:
#   * Captura errores de lectura/escritura
#   * Captura JSONDecodeError si el archivo no es JSON valido
#   * Imprime errores en consola
#   * Devuelve estructura vacia valida para que el programa continue
#
# Req 6:
# - Cumple PEP8 (imports ordenados, nombres claros, tipado).
#
# Req 7:
# - Codigo simple, sin imports sin uso, con docstrings y typing
#   para minimizar warnings en flake8 y pylint.
#

from __future__ import annotations

import json
import os
from json import JSONDecodeError
from typing import Any, Dict


def imprimir_error(mensaje: str) -> None:
    """
    Imprime un mensaje de error en consola.

    Req 5:
    - Los errores se muestran en consola.
    - No se lanza excepcion, la ejecucion continua.
    """
    print(f"[ERROR] {mensaje}")


class AlmacenJson:
    """
    Administra la lectura y escritura de un archivo JSON.

    Estructura esperada del archivo:
    {
      "hoteles": { "<id>": {...}, ... },
      "customers": { "<id>": {...}, ... },
      "reservations": { "<id>": {...}, ... }
    }

    Req 2:
    - Permite persistencia de datos en archivos.
    """

    def __init__(self, ruta_archivo: str) -> None:
        """
        Inicializa el almacen con la ruta del archivo.

        Args:
            ruta_archivo: ruta del archivo JSON.
        """
        self.ruta_archivo = ruta_archivo

    def cargar(self) -> Dict[str, Dict[str, Dict[str, Any]]]:
        """
        Carga la informacion desde el archivo JSON.

        Req 5:
        - Si el archivo no existe, devuelve estructura vacia valida.
        - Si el archivo esta corrupto, imprime error y devuelve estructura vacia.
        - Si la estructura es invalida, imprime error y normaliza a dict vacios.

        Retorna:
            Un dict con llaves:
            - hoteles
            - customers
            - reservations
        """
        if not os.path.exists(self.ruta_archivo):
            return {"hoteles": {}, "customers": {}, "reservations": {}}

        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except (OSError, JSONDecodeError) as error:
            imprimir_error(f"Archivo invalido o no legible: {error}")
            return {"hoteles": {}, "customers": {}, "reservations": {}}

        if not isinstance(datos, dict):
            imprimir_error("Estructura invalida: el JSON raiz no es un dict")
            return {"hoteles": {}, "customers": {}, "reservations": {}}

        hoteles = datos.get("hoteles", {})
        customers = datos.get("customers", {})
        reservations = datos.get("reservations", {})

        if not isinstance(hoteles, dict):
            imprimir_error("Estructura invalida: 'hoteles' no es un dict")
            hoteles = {}

        if not isinstance(customers, dict):
            imprimir_error("Estructura invalida: 'customers' no es un dict")
            customers = {}

        if not isinstance(reservations, dict):
            imprimir_error("Estructura invalida: 'reservations' no es un dict")
            reservations = {}

        return {"hoteles": hoteles, "customers": customers, "reservations": reservations}

    def guardar(self, datos: Dict[str, Dict[str, Dict[str, Any]]]) -> None:
        """
        Guarda la informacion en el archivo JSON.

        Req 2:
        - Implementa persistencia.

        Req 5:
        - Si falla la escritura, imprime error y continua.

        Args:
            datos: estructura completa del sistema a persistir.
        """
        try:
            with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, ensure_ascii=False, indent=2)
        except OSError as error:
            imprimir_error(f"No se pudo guardar el archivo: {error}")