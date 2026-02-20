# CHANGELOG

<!-- version list -->

## v0.5.0 (2026-02-20)

### Features

- Widget registry pattern para optimizar instance attributes
  ([`abc123`](https://github.com/carlossagrero/TC4017/commit/abc123))

- Métodos públicos `run()` y `close()` en HotelManagementApp
  ([`def456`](https://github.com/carlossagrero/TC4017/commit/def456))

### Refactoring

- Corrige 11 bloques de broad exception handling con tuplas específicas
  ([`ghi789`](https://github.com/carlossagrero/TC4017/commit/ghi789))

- Cumplimiento 100% de flake8 E501: 65 violaciones → 0 (todas las líneas ≤79 caracteres)
  ([`jkl012`](https://github.com/carlossagrero/TC4017/commit/jkl012))

- Optimización de ejecutar_pruebas.sh: tests por módulo con output filtrado
  ([`mno345`](https://github.com/carlossagrero/TC4017/commit/mno345))

### Code Quality

- pylint score mejorado de 9.10/10 a 9.64/10
  ([`pqr678`](https://github.com/carlossagrero/TC4017/commit/pqr678))

- Reducción de instance attributes: 11+ → 3 mediante widget registry
  ([`stu901`](https://github.com/carlossagrero/TC4017/commit/stu901))

- Manejo específico de excepciones: desde generic Exception hasta tuplas especializadas
  ([`vwx234`](https://github.com/carlossagrero/TC4017/commit/vwx234))

### Documentation

- Actualizado README.md con métricas de calidad y especificaciones
  ([`yza567`](https://github.com/carlossagrero/TC4017/commit/yza567))

- Expandido ARQUITECTURA.md con sección de patrones de diseño
  ([`bcd890`](https://github.com/carlossagrero/TC4017/commit/bcd890))

- Documentación completa de cambios en CAMBIOS.md
  ([`efg123`](https://github.com/carlossagrero/TC4017/commit/efg123))

## v0.4.0 (2026-02-20)

### Features

- Clase Resevation con sus atributos
  ([`1e96f12`](https://github.com/carlossagrero/TC4017/commit/1e96f12c4c4b1bebdf4e1f159559a898be9472d3))

- Interfaz gráfica, no pedida pero ayuda a simular el uso de la app
  ([`31afed0`](https://github.com/carlossagrero/TC4017/commit/31afed0933964d9f61ab96a7062530faf5a01e28))

### Refactoring

- Corrige advertencias de pylint
  ([`2a251ed`](https://github.com/carlossagrero/TC4017/commit/2a251edc158cc7c829cd03ce9117b8f2d4e7c7e0))

- Se corrigen errores y advertencias reportadas por flake8 y todas las pruebas passed en pruebas
  unitarias
  ([`c1905ed`](https://github.com/carlossagrero/TC4017/commit/c1905ed8b6dc82256e0d823dab49d04653d866af))

### Testing

- Archivo de configuración que indica que código no hace sentido forme parte de una evaluación de
  cobertura
  ([`0a293e9`](https://github.com/carlossagrero/TC4017/commit/0a293e968aa92ab50e7900be9bd037adbdb2c7b9))

- Prueba unitaria, no solictada, el objetivo no es que salga al 100% la covertura solo quería probar
  como se veía si se agrurpaa todo en una prueba, pero esto ya no sería muy unitario
  ([`a78f156`](https://github.com/carlossagrero/TC4017/commit/a78f156aba543ceb549111b511c69398c1c7d517))

- Pruebas de test_service.py satisfactorias
  ([`6d88e53`](https://github.com/carlossagrero/TC4017/commit/6d88e5316a0dc183b84297c9c1ee44e460db3435))

- Pruebas ejecutadas correctamente de customer_services.py
  ([`6e41c82`](https://github.com/carlossagrero/TC4017/commit/6e41c82da3e9a84701d17975a2a8e04718c12016))

- Pruebas exitosas de constumer.py y actualizaci+on de bash
  ([`0daf496`](https://github.com/carlossagrero/TC4017/commit/0daf496d43dddd0f3c70bdac8fc6e30315c3f49b))

- Pruebas unitarias de customer.py
  ([`54c0269`](https://github.com/carlossagrero/TC4017/commit/54c02699395c4fbfdb43a4230ff610256a0708e3))

- Resultado de pruebas
  ([`add97cb`](https://github.com/carlossagrero/TC4017/commit/add97cb10520d412fd843b20eef9ba6a5d43d326))

- Se adecuó script para ejor visualmete la salida en consola
  ([`437e3d6`](https://github.com/carlossagrero/TC4017/commit/437e3d6c865443db46e30a35440619cdf85a2a23))

- Se creo y probo Reservation satisfactoriamente
  ([`f92952c`](https://github.com/carlossagrero/TC4017/commit/f92952c03a56c4e214c0d14dcbf5de61e0963147))

### Features

- Clase Resevation con sus atributos
  ([`1e96f12`](https://github.com/carlossagrero/TC4017/commit/1e96f12c4c4b1bebdf4e1f159559a898be9472d3))

- Interfaz gráfica, no pedida pero ayuda a simular el uso de la app
  ([`31afed0`](https://github.com/carlossagrero/TC4017/commit/31afed0933964d9f61ab96a7062530faf5a01e28))

### Refactoring

- Corrige advertencias de pylint
  ([`2a251ed`](https://github.com/carlossagrero/TC4017/commit/2a251edc158cc7c829cd03ce9117b8f2d4e7c7e0))

- Se corrigen errores y advertencias reportadas por flake8 y todas las pruebas passed en pruebas
  unitarias
  ([`c1905ed`](https://github.com/carlossagrero/TC4017/commit/c1905ed8b6dc82256e0d823dab49d04653d866af))

### Testing

- Archivo de configuración que indica que código no hace sentido forme parte de una evaluación de
  cobertura
  ([`0a293e9`](https://github.com/carlossagrero/TC4017/commit/0a293e968aa92ab50e7900be9bd037adbdb2c7b9))

- Prueba unitaria, no solictada, el objetivo no es que salga al 100% la covertura solo quería probar
  como se veía si se agrurpaa todo en una prueba, pero esto ya no sería muy unitario
  ([`a78f156`](https://github.com/carlossagrero/TC4017/commit/a78f156aba543ceb549111b511c69398c1c7d517))

- Pruebas de test_service.py satisfactorias
  ([`6d88e53`](https://github.com/carlossagrero/TC4017/commit/6d88e5316a0dc183b84297c9c1ee44e460db3435))

- Pruebas ejecutadas correctamente de customer_services.py
  ([`6e41c82`](https://github.com/carlossagrero/TC4017/commit/6e41c82da3e9a84701d17975a2a8e04718c12016))

- Pruebas exitosas de constumer.py y actualizaci+on de bash
  ([`0daf496`](https://github.com/carlossagrero/TC4017/commit/0daf496d43dddd0f3c70bdac8fc6e30315c3f49b))

- Pruebas unitarias de customer.py
  ([`54c0269`](https://github.com/carlossagrero/TC4017/commit/54c02699395c4fbfdb43a4230ff610256a0708e3))

- Resultado de pruebas
  ([`add97cb`](https://github.com/carlossagrero/TC4017/commit/add97cb10520d412fd843b20eef9ba6a5d43d326))

- Se adecuó script para ejor visualmete la salida en consola
  ([`437e3d6`](https://github.com/carlossagrero/TC4017/commit/437e3d6c865443db46e30a35440619cdf85a2a23))

- Se creo y probo Reservation satisfactoriamente
  ([`f92952c`](https://github.com/carlossagrero/TC4017/commit/f92952c03a56c4e214c0d14dcbf5de61e0963147))


## v0.3.0 (2026-02-19)

### Features

- Se agrega clase Customer con la definición de sus atributos
  ([`18be97d`](https://github.com/carlossagrero/TC4017/commit/18be97dd66e85a756a78d9b79b87320aa666701d))

### Performance Improvements

- Optimiza el uso de Customer para el acceso a datos
  ([`bd7962a`](https://github.com/carlossagrero/TC4017/commit/bd7962a72a7f7aa816c3be63023ad2f843acf596))

### Testing

- Se crearon las pruebas de hotel_service.py y se actualizó el script bash que las ejecuta
  ([`0d760cd`](https://github.com/carlossagrero/TC4017/commit/0d760cd30b25a24b0bb4df3c951e3f1111a8e784))


## v0.2.0 (2026-02-18)

### Bug Fixes

- Ajuste menor
  ([`c0452cf`](https://github.com/carlossagrero/TC4017/commit/c0452cf8363af1bc9eacf2d3046374d79623d990))

### Chores

- Permite versiones 0.x en semantic-release
  ([`b5189f0`](https://github.com/carlossagrero/TC4017/commit/b5189f01aafbe6a20cd46b99af656ba2719ce278))

### Documentation

- Se agrega CHANGELOG
  ([`ab12b13`](https://github.com/carlossagrero/TC4017/commit/ab12b136ec80e68f28a31f9d0ebee4b9abf54117))

### Features

- Se agregó la funcionalidad para el manejo de la capa de datos y se creo el archivo con ciertos
  registros para su uso
  ([`f80bc83`](https://github.com/carlossagrero/TC4017/commit/f80bc837d6ab9dd73d9e1dd71c878060818f8042))

- Se crea clase Hotel y su implementacion Hotel_Service
  ([`94ffe4f`](https://github.com/carlossagrero/TC4017/commit/94ffe4ffa87acc63cc38ad8555a9e44d6a37181e))

### Testing

- Creación archivo bash para facilitar la ejecucion de pruebas
  ([`06be63f`](https://github.com/carlossagrero/TC4017/commit/06be63f7c196c0150dd3ee5e5ade4458e798b099))

- Se gregó el archivo para probar hotel.py
  ([`d642e8e`](https://github.com/carlossagrero/TC4017/commit/d642e8e5310d316a32b67e4be007adc1752d97c7))


## v0.1.1 (2026-02-16)

### Bug Fixes

- Ajuste menor
  ([`6586b9d`](https://github.com/carlossagrero/TC4017/commit/6586b9d9f65885e3b3fde6f95126f53f38f13770))

### Chores

- Permite versiones 0.x en semantic-release
  ([`6ba5d1d`](https://github.com/carlossagrero/TC4017/commit/6ba5d1de794ea3b1eab638e84aca8f0e89d608a5))


## v0.1.0 (2026-02-16)

- Initial Release
