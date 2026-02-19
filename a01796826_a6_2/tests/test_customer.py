import pytest

from src.customer import Customer


# Verifica la serializacion del customer a diccionario.
def test_a_dict_serializes_fields():
    customer = Customer(
        id_customer="C-1",
        nombre="Cliente Uno",
        email="cliente1@example.com",
        activo=False,
    )

    assert customer.a_dict() == {
        "id_customer": "C-1",
        "nombre": "Cliente Uno",
        "email": "cliente1@example.com",
        "activo": False,
    }


# Crea customers desde diccionarios validos.
@pytest.mark.parametrize(
    "payload, expected_activo",
    [
        (
            {
                "id_customer": "C-2",
                "nombre": "Cliente Dos",
                "email": "cliente2@example.com",
                "activo": True,
            },
            True,
        ),
        (
            {
                "id_customer": "C-3",
                "nombre": "Cliente Tres",
                "email": "cliente3@example.com",
            },
            True,
        ),
    ],
)
def test_desde_dict_creates_customer(payload, expected_activo):
    customer = Customer.desde_dict(payload)

    assert customer.id_customer == payload["id_customer"]
    assert customer.nombre == payload["nombre"]
    assert customer.email == payload["email"]
    assert customer.activo is expected_activo


# Falla si faltan llaves obligatorias.
@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"id_customer": "C-4"},
        {
            "id_customer": "C-5",
            "nombre": "Cliente Cinco",
        },
    ],
)
def test_desde_dict_missing_required_keys(payload):
    with pytest.raises(KeyError):
        Customer.desde_dict(payload)


# Falla si el email es invalido.
@pytest.mark.parametrize(
    "payload",
    [
        {
            "id_customer": "C-6",
            "nombre": "Cliente Seis",
            "email": "no-es-email",
        },
        {
            "id_customer": "C-7",
            "nombre": "Cliente Siete",
            "email": "sin-arroba.com",
        },
        {
            "id_customer": "C-8",
            "nombre": "Cliente Ocho",
            "email": "sin-punto@correo",
        },
    ],
)
def test_desde_dict_invalid_email(payload):
    with pytest.raises(ValueError):
        Customer.desde_dict(payload)
