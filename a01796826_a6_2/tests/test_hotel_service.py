import json

from src.hotel_service import HotelService


def _write_data(file_path, data):
    file_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


# Verifica que crear_hotel persiste los datos.
def test_crear_hotel_persists_data(tmp_path):
    #investigue que se puede usar esto para evitar escribir archivos reales 
    # en el sistema, y que pytest se encarga de limpiar 
    # el directorio temporal despues de la prueba.
    db_path = tmp_path / "bd.json"
    service = HotelService(str(db_path))

    hotel = service.crear_hotel("Hotel Uno", "Monterrey", 120)

    saved = json.loads(db_path.read_text(encoding="utf-8"))
    assert hotel.id_hotel in saved["hoteles"]
    assert saved["hoteles"][hotel.id_hotel] == {
        "id_hotel": hotel.id_hotel,
        "nombre": "Hotel Uno",
        "ciudad": "Monterrey",
        "total_habitaciones": 120,
        "activo": True,
    }


# Verifica que eliminar_hotel marca el hotel como inactivo.
def test_eliminar_hotel_marks_inactive(tmp_path):
    db_path = tmp_path / "bd.json"
    service = HotelService(str(db_path))
    hotel = service.crear_hotel("Hotel Dos", "CDMX", 80)

    result = service.eliminar_hotel(hotel.id_hotel)

    saved = json.loads(db_path.read_text(encoding="utf-8"))
    assert result is True
    assert saved["hoteles"][hotel.id_hotel]["activo"] is False


# Verifica que eliminar_hotel retorna False si no existe.
def test_eliminar_hotel_returns_false_when_missing(tmp_path):
    db_path = tmp_path / "bd.json"
    service = HotelService(str(db_path))

    assert service.eliminar_hotel("no-existe") is False


# Verifica que eliminar_hotel retorna False con datos corruptos.
def test_eliminar_hotel_returns_false_on_corrupt(tmp_path):
    db_path = tmp_path / "bd.json"
    _write_data(
        db_path,
        {
            "hoteles": {
                "H-1": {
                    "id_hotel": "H-1",
                    "nombre": "Hotel Tres",
                    "ciudad": "Guadalajara",
                    "total_habitaciones": -1,
                }
            }
        },
    )

    service = HotelService(str(db_path))

    assert service.eliminar_hotel("H-1") is False


# Verifica que mostrar_hotel devuelve un hotel valido.
def test_mostrar_hotel_returns_hotel(tmp_path):
    db_path = tmp_path / "bd.json"
    service = HotelService(str(db_path))
    hotel = service.crear_hotel("Hotel Cuatro", "Puebla", 50)

    found = service.mostrar_hotel(hotel.id_hotel)

    assert found is not None
    assert found.id_hotel == hotel.id_hotel
    assert found.nombre == "Hotel Cuatro"
    assert found.ciudad == "Puebla"
    assert found.total_habitaciones == 50
    assert found.activo is True


# Verifica que mostrar_hotel retorna None si no existe.
def test_mostrar_hotel_returns_none_when_missing(tmp_path):
    db_path = tmp_path / "bd.json"
    service = HotelService(str(db_path))

    assert service.mostrar_hotel("no-existe") is None


# Verifica que mostrar_hotel retorna None con datos corruptos.
def test_mostrar_hotel_returns_none_on_corrupt(tmp_path):
    db_path = tmp_path / "bd.json"
    _write_data(
        db_path,
        {
            "hoteles": {
                "H-2": {
                    "id_hotel": "H-2",
                    "nombre": "Hotel Cinco",
                    "ciudad": "Leon",
                    "total_habitaciones": "no-numerico",
                }
            }
        },
    )

    service = HotelService(str(db_path))

    assert service.mostrar_hotel("H-2") is None


# Verifica que modificar_hotel actualiza los campos.
def test_modificar_hotel_updates_fields(tmp_path):
    db_path = tmp_path / "bd.json"
    service = HotelService(str(db_path))
    hotel = service.crear_hotel("Hotel Seis", "Merida", 30)

    result = service.modificar_hotel(
        hotel.id_hotel,
        nombre="Hotel Seis Renovado",
        total_habitaciones=45,
    )

    saved = json.loads(db_path.read_text(encoding="utf-8"))
    assert result is True
    assert saved["hoteles"][hotel.id_hotel]["nombre"] == "Hotel Seis Renovado"
    assert saved["hoteles"][hotel.id_hotel]["ciudad"] == "Merida"
    assert saved["hoteles"][hotel.id_hotel]["total_habitaciones"] == 45


# Verifica que modificar_hotel retorna False si no existe.
def test_modificar_hotel_returns_false_when_missing(tmp_path):
    db_path = tmp_path / "bd.json"
    service = HotelService(str(db_path))

    assert service.modificar_hotel("no-existe", nombre="Nuevo") is False


# Verifica que modificar_hotel regresa False con datos corruptos.
def test_modificar_hotel_returns_false_on_corrupt(tmp_path):
    db_path = tmp_path / "bd.json"
    _write_data(
        db_path,
        {
            "hoteles": {
                "H-3": {
                    "id_hotel": "H-3",
                    "nombre": "Hotel Siete",
                    "ciudad": "Tijuana",
                    "total_habitaciones": -5,
                }
            }
        },
    )

    service = HotelService(str(db_path))

    assert service.modificar_hotel("H-3", nombre="Nuevo") is False
