import json

from src.customer_service import CustomerService
from src.hotel_service import HotelService
from src.reservation_service import ReservationService


def _write_data(file_path, data):
    file_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


# Verifica que crear_reservation persiste los datos y vincula customer con hotel.
def test_crear_reservation_persists_data(tmp_path):
    db_path = tmp_path / "bd.json"
    
    # Crear un customer y un hotel primero
    customer_service = CustomerService(str(db_path))
    hotel_service = HotelService(str(db_path))
    
    customer = customer_service.crear_customer("Cliente Test", "cliente@test.com")
    hotel = hotel_service.crear_hotel("Hotel Test", "Test City", 100)
    
    # Ahora crear la reservacion
    reservation_service = ReservationService(str(db_path))
    reservation = reservation_service.crear_reservation(customer.id_customer, hotel.id_hotel)

    saved = json.loads(db_path.read_text(encoding="utf-8"))
    assert reservation is not None
    assert reservation.id_reservation in saved["reservations"]
    assert saved["reservations"][reservation.id_reservation] == {
        "id_reservation": reservation.id_reservation,
        "id_customer": customer.id_customer,
        "id_hotel": hotel.id_hotel,
        "activo": True,
    }


# Verifica que crear_reservation retorna None si el customer no existe.
def test_crear_reservation_returns_none_when_customer_missing(tmp_path):
    db_path = tmp_path / "bd.json"
    
    hotel_service = HotelService(str(db_path))
    hotel = hotel_service.crear_hotel("Hotel Test", "Test City", 100)
    
    reservation_service = ReservationService(str(db_path))
    reservation = reservation_service.crear_reservation("no-existe", hotel.id_hotel)

    assert reservation is None


# Verifica que crear_reservation retorna None si el hotel no existe.
def test_crear_reservation_returns_none_when_hotel_missing(tmp_path):
    db_path = tmp_path / "bd.json"
    
    customer_service = CustomerService(str(db_path))
    customer = customer_service.crear_customer("Cliente Test", "cliente@test.com")
    
    reservation_service = ReservationService(str(db_path))
    reservation = reservation_service.crear_reservation(customer.id_customer, "no-existe")

    assert reservation is None


# Verifica que cancelar_reservation marca la reservacion como inactiva.
def test_cancelar_reservation_marks_inactive(tmp_path):
    db_path = tmp_path / "bd.json"
    
    customer_service = CustomerService(str(db_path))
    hotel_service = HotelService(str(db_path))
    reservation_service = ReservationService(str(db_path))
    
    customer = customer_service.crear_customer("Cliente Test", "cliente@test.com")
    hotel = hotel_service.crear_hotel("Hotel Test", "Test City", 100)
    reservation = reservation_service.crear_reservation(customer.id_customer, hotel.id_hotel)

    result = reservation_service.cancelar_reservation(reservation.id_reservation)

    saved = json.loads(db_path.read_text(encoding="utf-8"))
    assert result is True
    assert saved["reservations"][reservation.id_reservation]["activo"] is False


# Verifica que cancelar_reservation retorna False si no existe.
def test_cancelar_reservation_returns_false_when_missing(tmp_path):
    db_path = tmp_path / "bd.json"
    reservation_service = ReservationService(str(db_path))

    assert reservation_service.cancelar_reservation("no-existe") is False


# Verifica que cancelar_reservation retorna False con datos corruptos.
def test_cancelar_reservation_returns_false_on_corrupt(tmp_path):
    db_path = tmp_path / "bd.json"
    _write_data(
        db_path,
        {
            "reservations": {
                "R-1": {
                    "id_reservation": "R-1",
                    "id_customer": "C-1",
                    "id_hotel": "",
                }
            }
        },
    )

    reservation_service = ReservationService(str(db_path))

    assert reservation_service.cancelar_reservation("R-1") is False


# Verifica que mostrar_reservation devuelve una reservacion valida.
def test_mostrar_reservation_returns_reservation(tmp_path):
    db_path = tmp_path / "bd.json"
    
    customer_service = CustomerService(str(db_path))
    hotel_service = HotelService(str(db_path))
    reservation_service = ReservationService(str(db_path))
    
    customer = customer_service.crear_customer("Cliente Test", "cliente@test.com")
    hotel = hotel_service.crear_hotel("Hotel Test", "Test City", 100)
    reservation = reservation_service.crear_reservation(customer.id_customer, hotel.id_hotel)

    found = reservation_service.mostrar_reservation(reservation.id_reservation)

    assert found is not None
    assert found.id_reservation == reservation.id_reservation
    assert found.id_customer == customer.id_customer
    assert found.id_hotel == hotel.id_hotel
    assert found.activo is True


# Verifica que mostrar_reservation retorna None si no existe.
def test_mostrar_reservation_returns_none_when_missing(tmp_path):
    db_path = tmp_path / "bd.json"
    reservation_service = ReservationService(str(db_path))

    assert reservation_service.mostrar_reservation("no-existe") is None


# Verifica que mostrar_reservation retorna None con datos corruptos.
def test_mostrar_reservation_returns_none_on_corrupt(tmp_path):
    db_path = tmp_path / "bd.json"
    _write_data(
        db_path,
        {
            "reservations": {
                "R-2": {
                    "id_reservation": "R-2",
                    "id_customer": "C-2",
                    "id_hotel": "",
                }
            }
        },
    )

    reservation_service = ReservationService(str(db_path))

    assert reservation_service.mostrar_reservation("R-2") is None
