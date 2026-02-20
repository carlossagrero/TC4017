# Guía de Inicio Rápido - Aplicación de Escritorio

**Versión:** 0.5.0 (Mejorada con calidad de código)

## Iniciar la Aplicación

```bash
# Opción 1: Usar el script
src/ejecutar_app.sh

# Opción 2: Comando Python
python -m src.app_desktop

# Opción 3: Desde el directorio raíz
cd ruta/del/proyecto
python -m src.app_desktop
```

## Flujos de Trabajo Comunes

### 1. Crear un Cliente Nuevo

```
Pestaña: Clientes
1. Nombre: Juan Pérez
2. Email: juan.perez@email.com
3. Clic: "Crear Cliente"
```

**Resultado:**
```
✓ Cliente creado exitosamente
ID: a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6
Nombre: Juan Pérez
Email: juan.perez@email.com
Activo: True
```

**Guardar el ID:** Lo necesitará para crear reservaciones

---

### 2. Crear un Hotel Nuevo

```
Pestaña: Hoteles
1. Nombre: Hotel Stellar
2. Ciudad: Ciudad de México
3. Total Habitaciones: 150
4. Clic: "Crear Hotel"
```

**Resultado:**
```
✓ Hotel creado exitosamente
ID: x5y6z7a8-b9c0-d1e2-f3g4-h5i6j7k8l9m0
Nombre: Hotel Stellar
Ciudad: Ciudad de México
Habitaciones: 150
Activo: True
```

**Guardar el ID:** Lo necesitará para crear reservaciones

---

### 3. Crear una Reservación

```
Pestaña: Reservaciones
1. ID Cliente: a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6 
   (El que obtuvimos en el paso 1)
2. ID Hotel: x5y6z7a8-b9c0-d1e2-f3g4-h5i6j7k8l9m0
   (El que obtuvimos en el paso 2)
3. Clic: "Crear Reservación"
```

**Resultado:**
```
✓ Reservación creada exitosamente
ID: p1q2r3s4-t5u6-v7w8-x9y0-z1a2b3c4d5e6
Cliente ID: a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6
Hotel ID: x5y6z7a8-b9c0-d1e2-f3g4-h5i6j7k8l9m0
Activa: True
```

---

### 4. Buscar un Cliente

```
Pestaña: Clientes
1. ID Cliente: a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6
2. Clic: "Buscar Cliente"
```

**Resultado:**
```
ID: a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6
Nombre: Juan Pérez
Email: juan.perez@email.com
Activo: True
```

---

### 5. Modificar un Cliente

```
Pestaña: Clientes
1. ID Cliente: a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6
2. Nombre: Juan Carlos Pérez  (nuevo)
3. Dejar Email en blanco (no cambiar)
4. Clic: "Modificar Cliente"
```

**Resultado:**
```
✓ Cliente modificado exitosamente
```

**Nota:** Puede modificar solo algunos campos - deje en blanco los que no necesita cambiar

---

### 6. Ver una Reservación

```
Pestaña: Reservaciones
1. ID Reservación: p1q2r3s4-t5u6-v7w8-x9y0-z1a2b3c4d5e6
2. Clic: "Ver Reservación"
```

**Resultado:**
```
ID: p1q2r3s4-t5u6-v7w8-x9y0-z1a2b3c4d5e6
Cliente: Juan Pérez
Hotel: Hotel Stellar
Activa: True
```

---

### 7. Cancelar una Reservación

```
Pestaña: Reservaciones
1. ID Reservación: p1q2r3s4-t5u6-v7w8-x9y0-z1a2b3c4d5e6
2. Clic: "Cancelar Reservación"
3. Confirmar: Clic "Sí" en la ventana emergente
```

**Resultado:**
```
✓ Reservación cancelada exitosamente
```

---

### 8. Eliminar un Cliente

```
Pestaña: Clientes
1. ID Cliente: a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6
2. Clic: "Eliminar Cliente"
3. Confirmar: Clic "Sí" en la ventana emergente
```

**Resultado:**
```
✓ Cliente eliminado exitosamente
```

**Nota:** "Eliminar" es un borrado lógico - el cliente se marca como inactivo pero los datos permanecen en la base de datos

---

## Errores Comunes y Soluciones

### Error: "Arquitectura no compatible con tkinter"

**Causa:** Tkinter no está instalado

**Solución macOS:**
```bash
brew install python-tk@3.9  # (reemplazar 3.9 con su versión)
```

**Solución Linux:**
```bash
sudo apt-get update
sudo apt-get install python3-tk
```

---

### Error: "Email inválido"

**Causa:** El email no contiene "@" o "."

**Ejemplo incorrecto:** `juanperezemail.com`
**Ejemplo correcto:** `juan.perez@email.com`

---

### Error: "Habitaciones debe ser un número positivo"

**Causa:** Habitaciones debe ser un número entero > 0

**Ejemplo incorrecto:** `-50`, `0`, `12.5`
**Ejemplo correcto:** `50`, `100`, `150`

---

### Error: "Customer {ID} no existe"

**Causa:** Al crear una reservación, el cliente especificado no existe

**Solución:** 
1. Primero cree el cliente (Pestaña Clientes)
2. Copie el ID generado
3. Use ese ID en la reservación

---

### Error: "Hotel {ID} no existe"

**Causa:** Al crear una reservación, el hotel especificado no existe

**Solución:**
1. Primero cree el hotel (Pestaña Hoteles)
2. Copie el ID generado
3. Use ese ID en la reservación

---

## Consejos de Uso

### 💡 Mantener registro de IDs

Cuando cree clientes u hoteles, copie y guarde los IDs - los necesitará para reservaciones:

```
Cliente ID: [ID aquí]
Hotel ID: [ID aquí]
Reservación ID: [ID aquí]
```

### 💡 Usar "Buscar" antes de modificar

Busque un cliente/hotel antes de modificarlo para verificar que los datos son correctos:

1. Busque el cliente
2. Verifique que es el correcto
3. Luego modifique

### 💡 La aplicación es persistente

Los datos se guardan automáticamente en `data/bd.json`. Si cierra y vuelve a abrir la aplicación, los datos estarán ahí.

### 💡 Limpiar campos regularmente

Use "Limpiar" después de cada operación exitosa para evitar confusiones

---

## Estructura de Carpetas

```
proyecto/
├── src/
│   ├── app_desktop.py          ← NUEVA: Aplicación GUI
│   ├── __main__.py             ← NUEVA: Entry point
│   ├── customer.py
│   ├── customer_service.py
│   ├── hotel.py
│   ├── hotel_service.py
│   ├── reservation.py
│   ├── reservation_service.py
│   └── almacen_json.py
├── data/
│   └── bd.json                 ← Datos persistentes
├── tests/
│   └── ...
├── ejecutar_app.sh             ← NUEVA: Script para ejecutar
├── DESKTOP_APP_README.md       ← NUEVA: Documentación
└── ARQUITECTURA.md             ← NUEVA: Detalles técnicos
```

---

## Próximos Pasos

Después de instalar y probar:

1. Explore todas las funcionalidades
2. Cree varios clientes y hoteles
3. Haga pruebas de reservaciones
4. Verifique que los datos persisten al reiniciar
5. Consulte ARQUITECTURA.md para entender el diseño

---

## Mejoras Recientes (v0.5.0)

La aplicación ahora incluye mejoras de calidad de código:

- ✅ **pylint Score:** 9.64/10 (mejor)
- ✅ **flake8:** 0 violaciones (líneas ≤79 caracteres)
- ✅ **Excepciones:** Manejo específico y seguro
- ✅ **Arquitectura:** Widget registry pattern para mejor organización
- ✅ **API Pública:** Métodos `run()` y `close()` para testing

Para más detalles técnicos, consulte [ARQUITECTURA.md](ARQUITECTURA.md) o [CAMBIOS.md](CAMBIOS.md).
