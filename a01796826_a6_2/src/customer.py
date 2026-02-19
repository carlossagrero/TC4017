# customer.py
#
# ===============================
# CUMPLIMIENTO DE REQUISITOS
# ===============================
# Req 1, Req 2, Req 5, Req 6 y Req 7


from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass(frozen=True)
class Customer:
    """
    Representa un cliente del sistema.
    """

    id_customer: str
    nombre: str
    email: str
    activo: bool = True

    def a_dict(self) -> Dict[str, Any]:
        """
        Convierte el objeto Customer a un diccionario serializable a JSON.

        """
        return {
            "id_customer": self.id_customer,
            "nombre": self.nombre,
            "email": self.email,
            "activo": self.activo,
        }

    @staticmethod
    def desde_dict(datos: Dict[str, Any]) -> "Customer":
        """
        Crea un Customer desde un diccionario.

        """
        id_customer = str(datos["id_customer"])
        nombre = str(datos["nombre"])
        email = str(datos["email"])
        activo = bool(datos.get("activo", True))

        # Validacion simple de email
        if "@" not in email or "." not in email:
            raise ValueError("email invalido")

        return Customer(
            id_customer=id_customer,
            nombre=nombre,
            email=email,
            activo=activo,
        )