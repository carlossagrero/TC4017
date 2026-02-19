import pytest

from src.hotel import Hotel


# Verifica la serializacion del hotel a diccionario.
def test_a_dict_serializes_fields():
    hotel = Hotel(
        id_hotel="H-1",
        nombre="Hotel Uno",
        ciudad="Monterrey",
        total_habitaciones=120,
        activo=False,
    )

    assert hotel.a_dict() == {
        "id_hotel": "H-1",
        "nombre": "Hotel Uno",
        "ciudad": "Monterrey",
        "total_habitaciones": 120,
        "activo": False,
    }


# Crea hoteles desde diccionarios validos.
@pytest.mark.parametrize(
    "payload, expected_activo",
    [
        (
            {
                "id_hotel": "H-2",
                "nombre": "Hotel Dos",
                "ciudad": "Guadalajara",
                "total_habitaciones": 80,
                "activo": True,
            },
            True,
        ),
        (
            {
                "id_hotel": "H-3",
                "nombre": "Hotel Tres",
                "ciudad": "CDMX",
                "total_habitaciones": 0,
            },
            True,
        ),
    ],
)
def test_desde_dict_creates_hotel(payload, expected_activo):
    hotel = Hotel.desde_dict(payload)

    assert hotel.id_hotel == payload["id_hotel"]
    assert hotel.nombre == payload["nombre"]
    assert hotel.ciudad == payload["ciudad"]
    assert hotel.total_habitaciones == payload["total_habitaciones"]
    assert hotel.activo is expected_activo


# Falla si faltan llaves obligatorias.
@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"id_hotel": "H-4"},
        {
            "id_hotel": "H-5",
            "nombre": "Hotel Cinco",
            "ciudad": "Puebla",
        },
    ],
)
def test_desde_dict_missing_required_keys(payload):
    with pytest.raises(KeyError):
        Hotel.desde_dict(payload)


# Falla si total_habitaciones es invalido.
@pytest.mark.parametrize(
    "payload",
    [
        {
            "id_hotel": "H-6",
            "nombre": "Hotel Seis",
            "ciudad": "Merida",
            "total_habitaciones": -1,
        },
        {
            "id_hotel": "H-7",
            "nombre": "Hotel Siete",
            "ciudad": "Leon",
            "total_habitaciones": "no-numerico",
        },
    ],
)
def test_desde_dict_invalid_total_habitaciones(payload):
    with pytest.raises((ValueError, TypeError)):
        Hotel.desde_dict(payload)
