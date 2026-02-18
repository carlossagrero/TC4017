# hotel_service.py
#
# Req 1: Implementación de los métodos
# Req 2 (Hotels):
# Req 5:errores
# Req 6: PEP8
# Req 7:Que cunpla con pylint y con flake8
#

from __future__ import annotations

from typing import Any, Dict, Optional
from uuid import uuid4

from almacen_json import AlmacenJson, imprimir_error
from hotel import Hotel


def generar_id() -> str:
    """
    Genera un identificador unico para un hotel de forma
    semialeatoria usando uuid4.

    """
    return str(uuid4())


class HotelService:
    """
    Servicio responsable exclusivamente de la logica de Hotels.
    """
    def __init__(self, ruta_archivo: str) -> None:
        """
        Inicializa el servicio con un almacen JSON.

        """
        self.almacen = AlmacenJson(ruta_archivo)

    def _cargar(self) -> Dict[str, Dict[str, Dict[str, Any]]]:
        """
        Carga estructura completa desde el archivo.

        Req 5:
        - Si el archivo esta corrupto, AlmacenJson imprime error
          y devuelve estructura valida vacia.
        """
        return self.almacen.cargar()

    def _guardar(self, datos: Dict[str, Dict[str, Dict[str, Any]]]) -> None:
        """
        Guarda estructura completa en el archivo.

        Req 2:
        - Persistencia de datos.
        """
        self.almacen.guardar(datos)

    # =====================================================
    # Req 2.1.a  Create Hotel
    # =====================================================
    def crear_hotel(
        self,
        nombre: str,
        ciudad: str,
        total_habitaciones: int,
    ) -> Hotel:
        """
        Crea un nuevo hotel y lo guarda en el archivo.

        Req 2.1.a:
        - Implementa Create Hotel.
        """
        datos = self._cargar()
        datos.setdefault("hoteles", {})

        hotel = Hotel(
            id_hotel=generar_id(),
            nombre=nombre,
            ciudad=ciudad,
            total_habitaciones=int(total_habitaciones),
            activo=True,
        )

        datos["hoteles"][hotel.id_hotel] = hotel.a_dict()
        self._guardar(datos)

        return hotel

    # =====================================================
    # Req 2.1.b  Delete Hotel
    # =====================================================
    def eliminar_hotel(self, id_hotel: str) -> bool:
        """
        Realiza borrado logico (activo=False).

        Req 2.1.b:
        - Implementa Delete Hotel.

        Req 5:
        - Si el hotel esta corrupto en archivo,
          se imprime error y la ejecucion continua.
        """
        datos = self._cargar()
        hoteles = datos.setdefault("hoteles", {})
        hotel_dict = hoteles.get(id_hotel)

        if hotel_dict is None:
            return False

        try:
            hotel = Hotel.desde_dict(hotel_dict)
        except (KeyError, ValueError, TypeError) as error:
            imprimir_error(f"Hotel corrupto al eliminar: {error}")
            return False

        hotel_inactivo = Hotel(
            id_hotel=hotel.id_hotel,
            nombre=hotel.nombre,
            ciudad=hotel.ciudad,
            total_habitaciones=hotel.total_habitaciones,
            activo=False,
        )

        hoteles[id_hotel] = hotel_inactivo.a_dict()
        self._guardar(datos)

        return True

    # =====================================================
    # Req 2.1.c  Display Hotel information
    # =====================================================
    def mostrar_hotel(self, id_hotel: str) -> Optional[Hotel]:
        """
        Devuelve la informacion de un hotel.

        Req 2.1.c:
        - Implementa Display Hotel information.

        Req 5:
        - Si los datos estan corruptos,
          imprime error y retorna None.
        """
        datos = self._cargar()
        hoteles = datos.setdefault("hoteles", {})
        hotel_dict = hoteles.get(id_hotel)

        if hotel_dict is None:
            return None

        try:
            return Hotel.desde_dict(hotel_dict)
        except (KeyError, ValueError, TypeError) as error:
            imprimir_error(f"Hotel invalido en archivo: {error}")
            return None

    # =====================================================
    # Req 2.1.d  Modify Hotel Information
    # =====================================================
    def modificar_hotel(
        self,
        id_hotel: str,
        nombre: Optional[str] = None,
        ciudad: Optional[str] = None,
        total_habitaciones: Optional[int] = None,
    ) -> bool:
        """
        Modifica la informacion de un hotel existente.

        Req 2.1.d:
        - Implementa Modify Hotel Information.

        Req 5:
        - Si el registro esta corrupto,
          imprime error y retorna False.
        """
        datos = self._cargar()
        hoteles = datos.setdefault("hoteles", {})
        hotel_dict = hoteles.get(id_hotel)

        if hotel_dict is None:
            return False

        try:
            hotel = Hotel.desde_dict(hotel_dict)
        except (KeyError, ValueError, TypeError) as error:
            imprimir_error(f"Hotel invalido en archivo: {error}")
            return False

        hotel_actualizado = Hotel(
            id_hotel=hotel.id_hotel,
            nombre=nombre if nombre is not None else hotel.nombre,
            ciudad=ciudad if ciudad is not None else hotel.ciudad,
            total_habitaciones=(
                int(total_habitaciones)
                if total_habitaciones is not None
                else hotel.total_habitaciones
            ),
            activo=hotel.activo,
        )

        hoteles[id_hotel] = hotel_actualizado.a_dict()
        self._guardar(datos)

        return True