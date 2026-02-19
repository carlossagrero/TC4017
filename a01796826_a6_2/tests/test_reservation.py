import pytest

from src.reservation import Reservation


# Verifica la serializacion de la reservacion a diccionario.
def test_a_dict_serializes_fields():
    reservation = Reservation(
        id_reservation="R-1",
        id_customer="C-1",
        id_hotel="H-1",
        activo=False,
    )

    assert reservation.a_dict() == {
        "id_reservation": "R-1",
        "id_customer": "C-1",
        "id_hotel": "H-1",
        "activo": False,
    }


# Crea reservaciones desde diccionarios validos.
@pytest.mark.parametrize(
    "payload, expected_activo",
    [
        (
            {
                "id_reservation": "R-2",
                "id_customer": "C-2",
                "id_hotel": "H-2",
                "activo": True,
            },
            True,
        ),
        (
            {
                "id_reservation": "R-3",
                "id_customer": "C-3",
                "id_hotel": "H-3",
            },
            True,
        ),
    ],
)
def test_desde_dict_creates_reservation(payload, expected_activo):
    reservation = Reservation.desde_dict(payload)

    assert reservation.id_reservation == payload["id_reservation"]
    assert reservation.id_customer == payload["id_customer"]
    assert reservation.id_hotel == payload["id_hotel"]
    assert reservation.activo is expected_activo


# Falla si faltan llaves obligatorias.
@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"id_reservation": "R-4"},
        {
            "id_reservation": "R-5",
            "id_customer": "C-5",
        },
    ],
)
def test_desde_dict_missing_required_keys(payload):
    with pytest.raises(KeyError):
        Reservation.desde_dict(payload)


# Falla si los identificadores son vacios.
@pytest.mark.parametrize(
    "payload",
    [
        {
            "id_reservation": "",
            "id_customer": "C-6",
            "id_hotel": "H-6",
        },
        {
            "id_reservation": "R-7",
            "id_customer": "",
            "id_hotel": "H-7",
        },
        {
            "id_reservation": "R-8",
            "id_customer": "C-8",
            "id_hotel": "",
        },
    ],
)
def test_desde_dict_invalid_identifiers(payload):
    with pytest.raises(ValueError):
        Reservation.desde_dict(payload)
