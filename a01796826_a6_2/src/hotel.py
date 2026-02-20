"""Module for hotel reservation system."""
# Req 1: Clase Hotel definida aqui.
# Req 2: Decidí hacer una implementación usando dataclasses y métodos
# que conviertan objetos en diccionarios y viceversa, para facilitar la
# persistencia en JSON.
# Req 5: Validacion en desde_dict para detectar datos
# invalidos (se usa en administrador que continua).
# Req 6: Estilo PEP8 (nombres, largos de linea razonables, imports ordenados).
# Req 7: Sin patrones tipicos que generen warnings (docstrings, typing,
# no variables sin uso).

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass(frozen=True)
class Hotel:
    """
    Representa un hotel.

    Req 1: Abstraccion Hotel.
    """

    id_hotel: str
    nombre: str
    ciudad: str
    total_habitaciones: int
    activo: bool = True

    def a_dict(self) -> Dict[str, Any]:
        """
        Convierte el Hotel a un diccionario serializable a JSON.

        Req 2: Persistencia en archivos (se usa para guardar en JSON).
        """
        return {
            "id_hotel": self.id_hotel,
            "nombre": self.nombre,
            "ciudad": self.ciudad,
            "total_habitaciones": self.total_habitaciones,
            "activo": self.activo,
        }

    @staticmethod
    def desde_dict(datos: Dict[str, Any]) -> "Hotel":
        """
        Crea un Hotel desde un diccionario (normalmente leido
        desde archivo).

                Req 5: Manejo de datos invalidos:
                - Si el contenido es invalido, lanza excepcion
                    (KeyError/ValueError/TypeError)
          y el administrador captura e imprime error sin detener.

        Raises:
            KeyError, ValueError, TypeError
        """
        id_hotel = str(datos["id_hotel"])
        nombre = str(datos["nombre"])
        ciudad = str(datos["ciudad"])
        total_habitaciones = int(datos["total_habitaciones"])
        activo = bool(datos.get("activo", True))

        if total_habitaciones < 0:
            raise ValueError("total_habitaciones no puede ser negativo")

        return Hotel(
            id_hotel=id_hotel,
            nombre=nombre,
            ciudad=ciudad,
            total_habitaciones=total_habitaciones,
            activo=activo,
        )
