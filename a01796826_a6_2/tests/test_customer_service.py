import json

from src.customer_service import CustomerService


def _write_data(file_path, data):
    file_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


# Verifica que crear_customer persiste los datos.
def test_crear_customer_persists_data(tmp_path):
    db_path = tmp_path / "bd.json"
    service = CustomerService(str(db_path))

    customer = service.crear_customer("Cliente Uno", "cliente1@example.com")

    saved = json.loads(db_path.read_text(encoding="utf-8"))
    assert customer.id_customer in saved["customers"]
    assert saved["customers"][customer.id_customer] == {
        "id_customer": customer.id_customer,
        "nombre": "Cliente Uno",
        "email": "cliente1@example.com",
        "activo": True,
    }


# Verifica que eliminar_customer marca el customer como inactivo.
def test_eliminar_customer_marks_inactive(tmp_path):
    db_path = tmp_path / "bd.json"
    service = CustomerService(str(db_path))
    customer = service.crear_customer("Cliente Dos", "cliente2@example.com")

    result = service.eliminar_customer(customer.id_customer)

    saved = json.loads(db_path.read_text(encoding="utf-8"))
    assert result is True
    assert saved["customers"][customer.id_customer]["activo"] is False


# Verifica que eliminar_customer retorna False si no existe.
def test_eliminar_customer_returns_false_when_missing(tmp_path):
    db_path = tmp_path / "bd.json"
    service = CustomerService(str(db_path))

    assert service.eliminar_customer("no-existe") is False


# Verifica que eliminar_customer retorna False con datos corruptos.
def test_eliminar_customer_returns_false_on_corrupt(tmp_path):
    db_path = tmp_path / "bd.json"
    _write_data(
        db_path,
        {
            "customers": {
                "C-1": {
                    "id_customer": "C-1",
                    "nombre": "Cliente Tres",
                    "email": "no-es-email",
                }
            }
        },
    )

    service = CustomerService(str(db_path))

    assert service.eliminar_customer("C-1") is False


# Verifica que mostrar_customer devuelve un customer valido.
def test_mostrar_customer_returns_customer(tmp_path):
    db_path = tmp_path / "bd.json"
    service = CustomerService(str(db_path))
    customer = service.crear_customer("Cliente Cuatro", "cliente4@example.com")

    found = service.mostrar_customer(customer.id_customer)

    assert found is not None
    assert found.id_customer == customer.id_customer
    assert found.nombre == "Cliente Cuatro"
    assert found.email == "cliente4@example.com"
    assert found.activo is True


# Verifica que mostrar_customer retorna None si no existe.
def test_mostrar_customer_returns_none_when_missing(tmp_path):
    db_path = tmp_path / "bd.json"
    service = CustomerService(str(db_path))

    assert service.mostrar_customer("no-existe") is None


# Verifica que mostrar_customer retorna None con datos corruptos.
def test_mostrar_customer_returns_none_on_corrupt(tmp_path):
    db_path = tmp_path / "bd.json"
    _write_data(
        db_path,
        {
            "customers": {
                "C-2": {
                    "id_customer": "C-2",
                    "nombre": "Cliente Cinco",
                    "email": "sin-punto@correo",
                }
            }
        },
    )

    service = CustomerService(str(db_path))

    assert service.mostrar_customer("C-2") is None


# Verifica que modificar_customer actualiza los campos.
def test_modificar_customer_updates_fields(tmp_path):
    db_path = tmp_path / "bd.json"
    service = CustomerService(str(db_path))
    customer = service.crear_customer("Cliente Seis", "cliente6@example.com")

    result = service.modificar_customer(
        customer.id_customer,
        nombre="Cliente Seis Renovado",
        email="cliente6nuevo@example.com",
    )

    saved = json.loads(db_path.read_text(encoding="utf-8"))
    assert result is True
    assert saved["customers"][customer.id_customer]["nombre"] == "Cliente Seis Renovado"
    assert saved["customers"][customer.id_customer]["email"] == "cliente6nuevo@example.com"


# Verifica que modificar_customer retorna False si no existe.
def test_modificar_customer_returns_false_when_missing(tmp_path):
    db_path = tmp_path / "bd.json"
    service = CustomerService(str(db_path))

    assert service.modificar_customer("no-existe", nombre="Nuevo") is False


# Verifica que modificar_customer regresa False con datos corruptos.
def test_modificar_customer_returns_false_on_corrupt(tmp_path):
    db_path = tmp_path / "bd.json"
    _write_data(
        db_path,
        {
            "customers": {
                "C-3": {
                    "id_customer": "C-3",
                    "nombre": "Cliente Siete",
                    "email": "no-es-email",
                }
            }
        },
    )

    service = CustomerService(str(db_path))

    assert service.modificar_customer("C-3", nombre="Nuevo") is False


# Verifica que modificar_customer retorna False si email es invalido.
def test_modificar_customer_returns_false_on_invalid_email(tmp_path):
    db_path = tmp_path / "bd.json"
    service = CustomerService(str(db_path))
    customer = service.crear_customer("Cliente Ocho", "cliente8@example.com")

    assert service.modificar_customer(
        customer.id_customer,
        email="sin-punto@correo",
    ) is False
