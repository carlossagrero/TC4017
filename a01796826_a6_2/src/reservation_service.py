# reservation_service.py
#
# Implementa la lógica de Reservations para crear, cancelar y,
# aunque no pedida en los requerimeintos, mostrar info de una reservacion.
# ===============================
# CUMPLIMIENTO DE REQUISITOS
# ===============================
# Req 1, Req 2, Req 5, Req 6 y Req 7

from __future__ import annotations

from typing import Any, Dict, Optional
from uuid import uuid4

from .almacen_json import AlmacenJson, imprimir_error
from .reservation import Reservation


def generar_id() -> str:
    """
    Genera un identificador unico para una reservacion.
    """
    return str(uuid4())


class ReservationService:
    """
    Servicio responsable de operaciones de Reservations.
    """

    def __init__(self, ruta_archivo: str) -> None:
        """
        Inicializa el servicio con persistencia en archivo JSON.
        """
        self.almacen = AlmacenJson(ruta_archivo)

    def _cargar(self) -> Dict[str, Dict[str, Dict[str, Any]]]:
        """
        Carga estructura completa desde el archivo.
        """
        return self.almacen.cargar()

    def _guardar(self, datos: Dict[str, Dict[str, Dict[str, Any]]]) -> None:
        """
        Guarda estructura completa en el archivo.
        """
        self.almacen.guardar(datos)

    # =====================================================
    # Crear reservacion
    # =====================================================
    def crear_reservation(self, id_customer: str, id_hotel: str) -> Optional[Reservation]:
        """
        Crea una nueva reservacion vinculando un customer con un hotel.
        Retorna la reservacion creada o None si hay error.
        """
        datos = self._cargar()
        datos.setdefault("reservations", {})

        # Validar que el customer existe
        customers = datos.get("customers", {})
        if id_customer not in customers:
            imprimir_error(f"Customer {id_customer} no existe")
            return None

        # Validar que el hotel existe
        hoteles = datos.get("hoteles", {})
        if id_hotel not in hoteles:
            imprimir_error(f"Hotel {id_hotel} no existe")
            return None

        reservation = Reservation(
            id_reservation=generar_id(),
            id_customer=id_customer,
            id_hotel=id_hotel,
            activo=True,
        )

        datos["reservations"][reservation.id_reservation] = reservation.a_dict()
        self._guardar(datos)

        return reservation

    # =====================================================
    # Cancelar reservacion
    # =====================================================
    def cancelar_reservation(self, id_reservation: str) -> bool:
        """
        Cancela una reservacion (borrado logico, activo=False).
        """
        datos = self._cargar()
        reservations = datos.setdefault("reservations", {})
        reservation_dict = reservations.get(id_reservation)

        if reservation_dict is None:
            return False

        try:
            reservation = Reservation.desde_dict(reservation_dict)
        except (KeyError, ValueError, TypeError) as error:
            imprimir_error(f"Reservacion corrupta al cancelar: {error}")
            return False

        reservation_cancelada = Reservation(
            id_reservation=reservation.id_reservation,
            id_customer=reservation.id_customer,
            id_hotel=reservation.id_hotel,
            activo=False,
        )

        reservations[id_reservation] = reservation_cancelada.a_dict()
        self._guardar(datos)

        return True

    # =====================================================
    # Mostrar info de reservacion
    # =====================================================
    def mostrar_reservation(self, id_reservation: str) -> Optional[Reservation]:
        """
        Devuelve la informacion de una reservacion.
        """
        datos = self._cargar()
        reservations = datos.setdefault("reservations", {})
        reservation_dict = reservations.get(id_reservation)

        if reservation_dict is None:
            return None

        try:
            return Reservation.desde_dict(reservation_dict)
        except (KeyError, ValueError, TypeError) as error:
            imprimir_error(f"Reservacion invalida en archivo: {error}")
            return None
