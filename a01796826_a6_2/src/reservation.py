# reservation.py
#
# ===============================
# CUMPLIMIENTO DE REQUISITOS
# ===============================
# Req 1, Req 2, Req 5, Req 6 y Req 7

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass(frozen=True)
class Reservation:
    """
    Representa una reservacion entre un customer y un hotel.
    """

    id_reservation: str
    id_customer: str
    id_hotel: str
    activo: bool = True

    def a_dict(self) -> Dict[str, Any]:
        """
        Convierte el objeto Reservation a un diccionario serializable a JSON.

        """
        return {
            "id_reservation": self.id_reservation,
            "id_customer": self.id_customer,
            "id_hotel": self.id_hotel,
            "activo": self.activo,
        }

    @staticmethod
    def desde_dict(datos: Dict[str, Any]) -> "Reservation":
        """
        Crea una Reservation desde un diccionario.

        """
        id_reservation = str(datos["id_reservation"])
        id_customer = str(datos["id_customer"])
        id_hotel = str(datos["id_hotel"])
        activo = bool(datos.get("activo", True))

        if not id_reservation or not id_customer or not id_hotel:
            raise ValueError("identificadores invalidos")

        return Reservation(
            id_reservation=id_reservation,
            id_customer=id_customer,
            id_hotel=id_hotel,
            activo=activo,
        )
