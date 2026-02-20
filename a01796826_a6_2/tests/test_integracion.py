# tests/test_integracion.py
#
# Test de integración completo que prueba todos los componentes del sistema

import os
import sys
import json
import pytest
from pathlib import Path

# Configurar path para importar módulos desde src/
script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, script_dir)

from src.customer_service import CustomerService
from src.hotel_service import HotelService
from src.reservation_service import ReservationService
from src.almacen_json import AlmacenJson


@pytest.fixture
def bd_test_path():
    """
    Fixture que proporciona una ruta de BD de prueba limpia.
    Se ejecuta antes de cada test y limpia después.
    """
    data_dir = os.path.join(script_dir, "data")
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    bd_path = os.path.join(data_dir, "bd_integracion_test.json")
    
    # Limpiar BD antes del test
    if os.path.exists(bd_path):
        os.remove(bd_path)
    
    yield bd_path
    
    # Limpiar BD después del test
    if os.path.exists(bd_path):
        os.remove(bd_path)


@pytest.fixture
def services(bd_test_path):
    """
    Fixture que proporciona los tres servicios inicializados
    con la misma BD de prueba.
    """
    return {
        "customer": CustomerService(bd_test_path),
        "hotel": HotelService(bd_test_path),
        "reservation": ReservationService(bd_test_path),
        "bd_path": bd_test_path
    }


class TestIntegracionCompleta:
    """
    Suite de tests de integración que valida el funcionamiento
    completo del sistema de gestión de hoteles.
    """
    
    # ===== TESTS DE CREACIÓN =====
    
    def test_crear_cliente_valido(self, services):
        """Debe crear un cliente con datos válidos."""
        customer = services["customer"].crear_customer(
            nombre="Juan Pérez",
            email="juan@example.com"
        )
        
        assert customer is not None
        assert customer.nombre == "Juan Pérez"
        assert customer.email == "juan@example.com"
        assert customer.activo is True
        assert len(customer.id_customer) > 0
    
    def test_crear_hotel_valido(self, services):
        """Debe crear un hotel con datos válidos."""
        hotel = services["hotel"].crear_hotel(
            nombre="Hotel Paradise",
            ciudad="Miami",
            total_habitaciones=100
        )
        
        assert hotel is not None
        assert hotel.nombre == "Hotel Paradise"
        assert hotel.ciudad == "Miami"
        assert hotel.total_habitaciones == 100
        assert hotel.activo is True
        assert len(hotel.id_hotel) > 0
    
    def test_crear_reservacion_valida(self, services):
        """Debe crear una reservación vinculada a cliente y hotel existentes."""
        # Crear prerequisitos
        customer = services["customer"].crear_customer(
            nombre="María López",
            email="maria@example.com"
        )
        hotel = services["hotel"].crear_hotel(
            nombre="Hotel Deluxe",
            ciudad="Barcelona",
            total_habitaciones=50
        )
        
        # Crear reservación
        reservation = services["reservation"].crear_reservation(
            id_customer=customer.id_customer,
            id_hotel=hotel.id_hotel
        )
        
        assert reservation is not None
        assert reservation.id_customer == customer.id_customer
        assert reservation.id_hotel == hotel.id_hotel
        assert reservation.activo is True
        assert len(reservation.id_reservation) > 0
    
    # ===== TESTS DE BÚSQUEDA =====
    
    def test_buscar_cliente_existente(self, services):
        """Debe encontrar un cliente creado."""
        # Crear cliente
        customer_creado = services["customer"].crear_customer(
            nombre="Carlos Gómez",
            email="carlos@example.com"
        )
        
        # Buscar cliente
        customer_encontrado = services["customer"].mostrar_customer(
            customer_creado.id_customer
        )
        
        assert customer_encontrado is not None
        assert customer_encontrado.id_customer == customer_creado.id_customer
        assert customer_encontrado.nombre == "Carlos Gómez"
        assert customer_encontrado.email == "carlos@example.com"
    
    def test_buscar_cliente_inexistente(self, services):
        """Debe retornar None al buscar un cliente que no existe."""
        customer = services["customer"].mostrar_customer("id_inexistente")
        assert customer is None
    
    def test_buscar_hotel_existente(self, services):
        """Debe encontrar un hotel creado."""
        # Crear hotel
        hotel_creado = services["hotel"].crear_hotel(
            nombre="Hotel Royal",
            ciudad="Madrid",
            total_habitaciones=75
        )
        
        # Buscar hotel
        hotel_encontrado = services["hotel"].mostrar_hotel(hotel_creado.id_hotel)
        
        assert hotel_encontrado is not None
        assert hotel_encontrado.id_hotel == hotel_creado.id_hotel
        assert hotel_encontrado.nombre == "Hotel Royal"
        assert hotel_encontrado.ciudad == "Madrid"
        assert hotel_encontrado.total_habitaciones == 75
    
    def test_buscar_hotel_inexistente(self, services):
        """Debe retornar None al buscar un hotel que no existe."""
        hotel = services["hotel"].mostrar_hotel("id_inexistente")
        assert hotel is None
    
    def test_buscar_reservacion_existente(self, services):
        """Debe encontrar una reservación creada."""
        # Crear cliente y hotel
        customer = services["customer"].crear_customer(
            nombre="Ana Silva",
            email="ana@example.com"
        )
        hotel = services["hotel"].crear_hotel(
            nombre="Hotel Sunset",
            ciudad="Cancún",
            total_habitaciones=120
        )
        
        # Crear reservación
        reservation_creada = services["reservation"].crear_reservation(
            id_customer=customer.id_customer,
            id_hotel=hotel.id_hotel
        )
        
        # Buscar reservación
        reservation_encontrada = services["reservation"].mostrar_reservation(
            reservation_creada.id_reservation
        )
        
        assert reservation_encontrada is not None
        assert reservation_encontrada.id_reservation == reservation_creada.id_reservation
        assert reservation_encontrada.id_customer == customer.id_customer
        assert reservation_encontrada.id_hotel == hotel.id_hotel
        assert reservation_encontrada.activo is True
    
    def test_buscar_reservacion_inexistente(self, services):
        """Debe retornar None al buscar una reservación que no existe."""
        reservation = services["reservation"].mostrar_reservation("id_inexistente")
        assert reservation is None
    
    # ===== TESTS DE MODIFICACIÓN =====
    
    def test_modificar_cliente_nombre(self, services):
        """Debe modificar el nombre de un cliente."""
        # Crear cliente
        customer = services["customer"].crear_customer(
            nombre="Luis García",
            email="luis@example.com"
        )
        
        # Modificar
        success = services["customer"].modificar_customer(
            customer.id_customer,
            nombre="Luis García Pérez"
        )
        assert success is True
        
        # Verificar
        customer_actualizado = services["customer"].mostrar_customer(
            customer.id_customer
        )
        assert customer_actualizado.nombre == "Luis García Pérez"
        assert customer_actualizado.email == "luis@example.com"
    
    def test_modificar_cliente_email(self, services):
        """Debe modificar el email de un cliente."""
        # Crear cliente
        customer = services["customer"].crear_customer(
            nombre="Rosa Martínez",
            email="rosa@example.com"
        )
        
        # Modificar
        success = services["customer"].modificar_customer(
            customer.id_customer,
            email="rosa.martinez@example.com"
        )
        assert success is True
        
        # Verificar
        customer_actualizado = services["customer"].mostrar_customer(
            customer.id_customer
        )
        assert customer_actualizado.nombre == "Rosa Martínez"
        assert customer_actualizado.email == "rosa.martinez@example.com"
    
    def test_modificar_cliente_nombre_y_email(self, services):
        """Debe modificar nombre y email de un cliente simultáneamente."""
        # Crear cliente
        customer = services["customer"].crear_customer(
            nombre="Pedro López",
            email="pedro@example.com"
        )
        
        # Modificar ambos
        success = services["customer"].modificar_customer(
            customer.id_customer,
            nombre="Pedro López García",
            email="pedro.garcia@example.com"
        )
        assert success is True
        
        # Verificar
        customer_actualizado = services["customer"].mostrar_customer(
            customer.id_customer
        )
        assert customer_actualizado.nombre == "Pedro López García"
        assert customer_actualizado.email == "pedro.garcia@example.com"
    
    def test_modificar_hotel_nombre(self, services):
        """Debe modificar el nombre de un hotel."""
        hotel = services["hotel"].crear_hotel(
            nombre="Hotel Antiguo",
            ciudad="Sevilla",
            total_habitaciones=60
        )
        
        success = services["hotel"].modificar_hotel(
            id_hotel=hotel.id_hotel,
            nombre="Hotel Nuevo"
        )
        assert success is True
        
        hotel_actualizado = services["hotel"].mostrar_hotel(hotel.id_hotel)
        assert hotel_actualizado.nombre == "Hotel Nuevo"
        assert hotel_actualizado.ciudad == "Sevilla"
        assert hotel_actualizado.total_habitaciones == 60
    
    def test_modificar_hotel_ciudad(self, services):
        """Debe modificar la ciudad de un hotel."""
        hotel = services["hotel"].crear_hotel(
            nombre="Hotel Central",
            ciudad="Valencia",
            total_habitaciones=80
        )
        
        success = services["hotel"].modificar_hotel(
            id_hotel=hotel.id_hotel,
            ciudad="Bilbao"
        )
        assert success is True
        
        hotel_actualizado = services["hotel"].mostrar_hotel(hotel.id_hotel)
        assert hotel_actualizado.nombre == "Hotel Central"
        assert hotel_actualizado.ciudad == "Bilbao"
        assert hotel_actualizado.total_habitaciones == 80
    
    def test_modificar_hotel_habitaciones(self, services):
        """Debe modificar el total de habitaciones de un hotel."""
        hotel = services["hotel"].crear_hotel(
            nombre="Hotel Renovado",
            ciudad="Granada",
            total_habitaciones=50
        )
        
        success = services["hotel"].modificar_hotel(
            id_hotel=hotel.id_hotel,
            total_habitaciones=100
        )
        assert success is True
        
        hotel_actualizado = services["hotel"].mostrar_hotel(hotel.id_hotel)
        assert hotel_actualizado.nombre == "Hotel Renovado"
        assert hotel_actualizado.ciudad == "Granada"
        assert hotel_actualizado.total_habitaciones == 100
    
    def test_modificar_hotel_todos_los_campos(self, services):
        """Debe modificar todos los campos de un hotel."""
        hotel = services["hotel"].crear_hotel(
            nombre="Hotel Viejo",
            ciudad="Toledo",
            total_habitaciones=40
        )
        
        success = services["hotel"].modificar_hotel(
            id_hotel=hotel.id_hotel,
            nombre="Hotel Moderno",
            ciudad="Cuenca",
            total_habitaciones=90
        )
        assert success is True
        
        hotel_actualizado = services["hotel"].mostrar_hotel(hotel.id_hotel)
        assert hotel_actualizado.nombre == "Hotel Moderno"
        assert hotel_actualizado.ciudad == "Cuenca"
        assert hotel_actualizado.total_habitaciones == 90
    
    # ===== TESTS DE ELIMINACIÓN =====
    
    def test_eliminar_cliente(self, services):
        """Debe realizar borrado lógico de un cliente."""
        customer = services["customer"].crear_customer(
            nombre="Federico Ruiz",
            email="federico@example.com"
        )
        
        # Eliminar
        success = services["customer"].eliminar_customer(customer.id_customer)
        assert success is True
        
        # Verificar borrado lógico
        customer_eliminado = services["customer"].mostrar_customer(
            customer.id_customer
        )
        assert customer_eliminado is not None
        assert customer_eliminado.activo is False
    
    def test_eliminar_hotel(self, services):
        """Debe realizar borrado lógico de un hotel."""
        hotel = services["hotel"].crear_hotel(
            nombre="Hotel Temporal",
            ciudad="Córdoba",
            total_habitaciones=70
        )
        
        # Eliminar
        success = services["hotel"].eliminar_hotel(hotel.id_hotel)
        assert success is True
        
        # Verificar borrado lógico
        hotel_eliminado = services["hotel"].mostrar_hotel(hotel.id_hotel)
        assert hotel_eliminado is not None
        assert hotel_eliminado.activo is False
    
    # ===== TESTS DE CANCELACIÓN DE RESERVACIONES =====
    
    def test_cancelar_reservacion(self, services):
        """Debe cancelar una reservación (borrado lógico)."""
        # Crear cliente y hotel
        customer = services["customer"].crear_customer(
            nombre="Sandra Núñez",
            email="sandra@example.com"
        )
        hotel = services["hotel"].crear_hotel(
            nombre="Hotel Cancelable",
            ciudad="Alicante",
            total_habitaciones=55
        )
        
        # Crear reservación
        reservation = services["reservation"].crear_reservation(
            id_customer=customer.id_customer,
            id_hotel=hotel.id_hotel
        )
        
        # Cancelar
        success = services["reservation"].cancelar_reservation(
            reservation.id_reservation
        )
        assert success is True
        
        # Verificar cancelación
        reservation_cancelada = services["reservation"].mostrar_reservation(
            reservation.id_reservation
        )
        assert reservation_cancelada is not None
        assert reservation_cancelada.activo is False
    
    # ===== TESTS DE PERSISTENCIA =====
    
    def test_persistencia_cliente_en_bd(self, services):
        """Debe persistir un cliente en la BD JSON."""
        customer = services["customer"].crear_customer(
            nombre="Miguel Ángel",
            email="miguel@example.com"
        )
        
        # Verificar archivo BD
        bd_path = services["bd_path"]
        assert os.path.exists(bd_path)
        
        with open(bd_path, 'r') as f:
            data = json.load(f)
        
        assert "customers" in data
        assert customer.id_customer in data["customers"]
    
    def test_persistencia_hotel_en_bd(self, services):
        """Debe persistir un hotel en la BD JSON."""
        hotel = services["hotel"].crear_hotel(
            nombre="Hotel Persistente",
            ciudad="Valladolid",
            total_habitaciones=110
        )
        
        # Verificar archivo BD
        bd_path = services["bd_path"]
        assert os.path.exists(bd_path)
        
        with open(bd_path, 'r') as f:
            data = json.load(f)
        
        assert "hoteles" in data
        assert hotel.id_hotel in data["hoteles"]
    
    def test_persistencia_reservacion_en_bd(self, services):
        """Debe persistir una reservación en la BD JSON."""
        customer = services["customer"].crear_customer(
            nombre="Elena Sánchez",
            email="elena@example.com"
        )
        hotel = services["hotel"].crear_hotel(
            nombre="Hotel Permanente",
            ciudad="Zamora",
            total_habitaciones=45
        )
        
        reservation = services["reservation"].crear_reservation(
            id_customer=customer.id_customer,
            id_hotel=hotel.id_hotel
        )
        
        # Verificar archivo BD
        bd_path = services["bd_path"]
        assert os.path.exists(bd_path)
        
        with open(bd_path, 'r') as f:
            data = json.load(f)
        
        assert "reservations" in data
        assert reservation.id_reservation in data["reservations"]
    
    # ===== TESTS DE FLUJO COMPLETO =====
    
    def test_flujo_completo_crud(self, services):
        """
        Test de integración completo que valida:
        - Crear múltiples clientes y hoteles
        - Crear reservaciones
        - Buscar registros
        - Modificar registros
        - Eliminar registros
        - Verificar persistencia
        """
        bd_path = services["bd_path"]
        
        # 1. Crear 2 clientes
        customer1 = services["customer"].crear_customer(
            nombre="Cliente Uno",
            email="cliente1@example.com"
        )
        customer2 = services["customer"].crear_customer(
            nombre="Cliente Dos",
            email="cliente2@example.com"
        )
        assert customer1.id_customer != customer2.id_customer
        
        # 2. Crear 2 hoteles
        hotel1 = services["hotel"].crear_hotel(
            nombre="Hotel Uno",
            ciudad="Ciudad A",
            total_habitaciones=100
        )
        hotel2 = services["hotel"].crear_hotel(
            nombre="Hotel Dos",
            ciudad="Ciudad B",
            total_habitaciones=150
        )
        assert hotel1.id_hotel != hotel2.id_hotel
        
        # 3. Crear 3 reservaciones
        res1 = services["reservation"].crear_reservation(
            id_customer=customer1.id_customer,
            id_hotel=hotel1.id_hotel
        )
        res2 = services["reservation"].crear_reservation(
            id_customer=customer2.id_customer,
            id_hotel=hotel1.id_hotel
        )
        res3 = services["reservation"].crear_reservation(
            id_customer=customer2.id_customer,
            id_hotel=hotel2.id_hotel
        )
        assert res1.id_reservation != res2.id_reservation != res3.id_reservation
        
        # 4. Modificar cliente
        services["customer"].modificar_customer(
            customer1.id_customer,
            nombre="Cliente Uno Actualizado"
        )
        customer1_mod = services["customer"].mostrar_customer(customer1.id_customer)
        assert customer1_mod.nombre == "Cliente Uno Actualizado"
        
        # 5. Modificar hotel
        services["hotel"].modificar_hotel(
            id_hotel=hotel1.id_hotel,
            total_habitaciones=200
        )
        hotel1_mod = services["hotel"].mostrar_hotel(hotel1.id_hotel)
        assert hotel1_mod.total_habitaciones == 200
        
        # 6. Cancelar reservación
        services["reservation"].cancelar_reservation(res1.id_reservation)
        res1_cancelada = services["reservation"].mostrar_reservation(
            res1.id_reservation
        )
        assert res1_cancelada.activo is False
        
        # 7. Eliminar cliente
        services["customer"].eliminar_customer(customer2.id_customer)
        customer2_eliminado = services["customer"].mostrar_customer(
            customer2.id_customer
        )
        assert customer2_eliminado.activo is False
        
        # 8. Verificar persistencia
        assert os.path.exists(bd_path)
        with open(bd_path, 'r') as f:
            data = json.load(f)
        
        assert len(data.get("customers", {})) == 2
        assert len(data.get("hoteles", {})) == 2
        assert len(data.get("reservations", {})) == 3


class TestAlmacenJson:
    """
    Suite de tests para validar el almacenamiento JSON y manejo de errores.
    """
    
    def test_cargar_archivo_inexistente(self):
        """Debe retornar estructura vacía si el archivo no existe."""
        almacen = AlmacenJson("/ruta/inexistente/archivo.json")
        datos = almacen.cargar()
        
        assert datos == {
            "hoteles": {},
            "customers": {},
            "reservations": {}
        }
    
    def test_guardar_crea_archivo(self):
        """Debe crear un archivo JSON con los datos proporcionados."""
        ruta_temp = os.path.join(script_dir, "data", "test_guardar.json")
        almacen = AlmacenJson(ruta_temp)
        
        datos = {
            "hoteles": {"h1": {"id": "h1", "nombre": "Hotel Test"}},
            "customers": {"c1": {"id": "c1", "nombre": "Cliente Test"}},
            "reservations": {}
        }
        
        almacen.guardar(datos)
        
        assert os.path.exists(ruta_temp)
        
        with open(ruta_temp, 'r') as f:
            datos_guardados = json.load(f)
        
        assert datos_guardados == datos
        
        # Limpiar
        os.remove(ruta_temp)
    
    def test_cargar_archivo_corrupto(self, capsys):
        """Debe retornar estructura vacía y mostrar error si JSON es corrupto."""
        ruta_temp = os.path.join(script_dir, "data", "test_corrupto.json")
        
        # Crear archivo corrupto
        with open(ruta_temp, 'w') as f:
            f.write("{ corrupto json invalido ]")
        
        almacen = AlmacenJson(ruta_temp)
        datos = almacen.cargar()
        
        # Debe retornar estructura vacía
        assert datos == {
            "hoteles": {},
            "customers": {},
            "reservations": {}
        }
        
        # Debe haber mostrado error
        captured = capsys.readouterr()
        assert "[ERROR]" in captured.out
        
        # Limpiar
        os.remove(ruta_temp)
    
    def test_cargar_estructura_invalida_no_dict(self, capsys):
        """Debe retornar estructura vacía si el JSON raíz no es dict."""
        ruta_temp = os.path.join(script_dir, "data", "test_no_dict.json")
        
        # Crear archivo con valor inválido
        with open(ruta_temp, 'w') as f:
            json.dump([1, 2, 3], f)
        
        almacen = AlmacenJson(ruta_temp)
        datos = almacen.cargar()
        
        assert datos == {
            "hoteles": {},
            "customers": {},
            "reservations": {}
        }
        
        captured = capsys.readouterr()
        assert "[ERROR]" in captured.out
        
        os.remove(ruta_temp)
    
    def test_cargar_estructura_invalida_hoteles_no_dict(self, capsys):
        """Debe normalizar si 'hoteles' no es dict."""
        ruta_temp = os.path.join(script_dir, "data", "test_hoteles_invalid.json")
        
        datos_corrupto = {
            "hoteles": [1, 2, 3],  # Debe ser dict
            "customers": {},
            "reservations": {}
        }
        
        with open(ruta_temp, 'w') as f:
            json.dump(datos_corrupto, f)
        
        almacen = AlmacenJson(ruta_temp)
        datos = almacen.cargar()
        
        # Debe normalizar a dict vacío
        assert isinstance(datos["hoteles"], dict)
        assert datos["hoteles"] == {}
        assert datos["customers"] == {}
        assert datos["reservations"] == {}
        
        captured = capsys.readouterr()
        assert "[ERROR]" in captured.out
        
        os.remove(ruta_temp)
    
    def test_cargar_estructura_invalida_customers_no_dict(self, capsys):
        """Debe normalizar si 'customers' no es dict."""
        ruta_temp = os.path.join(script_dir, "data", "test_customers_invalid.json")
        
        datos_corrupto = {
            "hoteles": {},
            "customers": "no es dict",
            "reservations": {}
        }
        
        with open(ruta_temp, 'w') as f:
            json.dump(datos_corrupto, f)
        
        almacen = AlmacenJson(ruta_temp)
        datos = almacen.cargar()
        
        assert isinstance(datos["customers"], dict)
        assert datos["customers"] == {}
        
        captured = capsys.readouterr()
        assert "[ERROR]" in captured.out
        
        os.remove(ruta_temp)
    
    def test_cargar_estructura_invalida_reservations_no_dict(self, capsys):
        """Debe normalizar si 'reservations' no es dict."""
        ruta_temp = os.path.join(script_dir, "data", "test_reservations_invalid.json")
        
        datos_corrupto = {
            "hoteles": {},
            "customers": {},
            "reservations": 123
        }
        
        with open(ruta_temp, 'w') as f:
            json.dump(datos_corrupto, f)
        
        almacen = AlmacenJson(ruta_temp)
        datos = almacen.cargar()
        
        assert isinstance(datos["reservations"], dict)
        assert datos["reservations"] == {}
        
        captured = capsys.readouterr()
        assert "[ERROR]" in captured.out
        
        os.remove(ruta_temp)
    
    def test_cargar_archivo_faltando_claves(self):
        """Debe retornar estructura completa aunque falten claves."""
        ruta_temp = os.path.join(script_dir, "data", "test_claves_faltantes.json")
        
        datos_incompleto = {
            "hoteles": {"h1": {}}
        }
        
        with open(ruta_temp, 'w') as f:
            json.dump(datos_incompleto, f)
        
        almacen = AlmacenJson(ruta_temp)
        datos = almacen.cargar()
        
        # Debe tener todas las claves
        assert "hoteles" in datos
        assert "customers" in datos
        assert "reservations" in datos
        
        os.remove(ruta_temp)
    
    def test_guardar_y_cargar_consistency(self):
        """Debe mantener consistencia entre guardar y cargar."""
        ruta_temp = os.path.join(script_dir, "data", "test_consistency.json")
        almacen = AlmacenJson(ruta_temp)
        
        datos_original = {
            "hoteles": {
                "h1": {"id_hotel": "h1", "nombre": "Hotel A", "ciudad": "Madrid"},
                "h2": {"id_hotel": "h2", "nombre": "Hotel B", "ciudad": "Barcelona"}
            },
            "customers": {
                "c1": {"id_customer": "c1", "nombre": "Cliente A", "email": "a@test.com"},
                "c2": {"id_customer": "c2", "nombre": "Cliente B", "email": "b@test.com"}
            },
            "reservations": {
                "r1": {"id_reservation": "r1", "id_customer": "c1", "id_hotel": "h1"}
            }
        }
        
        # Guardar
        almacen.guardar(datos_original)
        
        # Cargar
        datos_cargados = almacen.cargar()
        
        # Deben ser idénticos
        assert datos_cargados == datos_original
        
        os.remove(ruta_temp)
