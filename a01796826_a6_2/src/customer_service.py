# customer_service.py
#
# Implementa la lógica de Customers  en una clase CustomerService,
#
# ===============================
# CUMPLIMIENTO DE REQUISITOS
# ===============================
# Req 1, Req 2, Req 5, Req 6 y Req 7

from __future__ import annotations

from typing import Any, Dict, Optional
from uuid import uuid4

from .almacen_json import AlmacenJson, imprimir_error
from .customer import Customer


def generar_id() -> str:
    """
    Genera un identificador unico para un customer.
    """
    return str(uuid4())


class CustomerService:
    """
    Servicio responsable de operaciones de Customers.
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
    # Crear cliente
    # =====================================================
    def crear_customer(self, nombre: str, email: str) -> Customer:
        """
        Crea un nuevo customer y lo persiste.
        """
        datos = self._cargar()
        datos.setdefault("customers", {})

        customer = Customer(
            id_customer=generar_id(),
            nombre=nombre,
            email=email,
            activo=True,
        )

        datos["customers"][customer.id_customer] = customer.a_dict()
        self._guardar(datos)

        return customer

    # =====================================================
    # Borrar cliete o más bien inhabiliar
    # =====================================================
    def eliminar_customer(self, id_customer: str) -> bool:
        """
        Elimina (borrado lógico) no en el archivo un customer marcandolo como inactivo.
        """
        datos = self._cargar()
        customers = datos.setdefault("customers", {})
        customer_dict = customers.get(id_customer)

        if customer_dict is None:
            return False

        try:
            customer = Customer.desde_dict(customer_dict)
        except (KeyError, ValueError, TypeError) as error:
            imprimir_error(f"Customer corrupto al eliminar: {error}")
            return False

        customer_inactivo = Customer(
            id_customer=customer.id_customer,
            nombre=customer.nombre,
            email=customer.email,
            activo=False,
        )

        customers[id_customer] = customer_inactivo.a_dict()
        self._guardar(datos)

        return True

    # =====================================================
    # Mostrar info de cliente
    # =====================================================
    def mostrar_customer(self, id_customer: str) -> Optional[Customer]:
        """
        Muestra la informacion de un customer.

        """
        datos = self._cargar()
        customers = datos.setdefault("customers", {})
        customer_dict = customers.get(id_customer)

        if customer_dict is None:
            return None

        try:
            return Customer.desde_dict(customer_dict)
        except (KeyError, ValueError, TypeError) as error:
            imprimir_error(f"Customer invalido en archivo: {error}")
            return None

    # =====================================================
    # Actualizar info de cliente
    # =====================================================
    def modificar_customer(
        self,
        id_customer: str,
        nombre: Optional[str] = None,
        email: Optional[str] = None,
    ) -> bool:
        """
        Modifica la informacion de un customer.

        """
        datos = self._cargar()
        customers = datos.setdefault("customers", {})
        customer_dict = customers.get(id_customer)

        if customer_dict is None:
            return False

        try:
            customer = Customer.desde_dict(customer_dict)
        except (KeyError, ValueError, TypeError) as error:
            imprimir_error(f"Customer invalido en archivo: {error}")
            return False

        nuevo_email = email if email is not None else customer.email
        if "@" not in nuevo_email or "." not in nuevo_email:
            imprimir_error("Email invalido al modificar customer")
            return False

        customer_actualizado = Customer(
            id_customer=customer.id_customer,
            nombre=nombre if nombre is not None else customer.nombre,
            email=nuevo_email,
            activo=customer.activo,
        )

        customers[id_customer] = customer_actualizado.a_dict()
        self._guardar(datos)

        return True