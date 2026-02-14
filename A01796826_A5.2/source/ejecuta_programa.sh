#!/bin/bash

# Ruta del catálogo de precios
CATALOGO="../data/priceCatalogue.json"

# Iterar sobre todos los archivos *.json en data/ excepto priceCatalogue.json
for archivo_ventas in ../data/*.json; do
    # Omitir el archivo de catálogo
    if [[ "$(basename "$archivo_ventas")" == "priceCatalogue.json" ]]; then
        continue
    fi

    # Obtener nombre del archivo sin extensión
    nombre_archivo=$(basename "$archivo_ventas" .json)
    archivo_salida="../results/${nombre_archivo}_results.txt"

    echo "===== $(date) =====" | tee -a ../tests/bitacora_ejecucion.txt
    echo ">>> Procesando: $archivo_ventas" | tee -a ../tests/bitacora_ejecucion.txt
    echo ">>> Archivo de salida: $archivo_salida" | tee -a ../tests/bitacora_ejecucion.txt
    python3 computeSales.py "$CATALOGO" "$archivo_ventas" "$archivo_salida" 2>&1 | tee -a ../tests/bitacora_ejecucion.txt
    echo "" | tee -a ../tests/bitacora_ejecucion.txt
done

echo "===== $(date) =====" | tee -a ../tests/pylint_historial.txt
echo ">>> Ejecutando pylint..." | tee -a ../tests/pylint_historial.txt
pylint computeSales.py | tee -a ../tests/pylint_historial.txt
echo "" | tee -a ../tests/pylint_historial.txt

echo "===== $(date) =====" | tee -a ../tests/flake8_historial.txt
echo ">>> Ejecutando Flake8..." | tee -a ../tests/flake8_historial.txt
flake8 computeSales.py | tee -a ../tests/flake8_historial.txt
echo "" | tee -a ../tests/flake8_historial.txt