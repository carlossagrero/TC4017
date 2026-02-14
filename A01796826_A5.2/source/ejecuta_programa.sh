#!/bin/bash

echo "===== $(date) =====" | tee -a ../tests/bitacora_ejecucion.txt
echo ">>> Ejecutando programa Python..." | tee -a ../tests/bitacora_ejecucion.txt
python3 computeSales.py ../data/priceCatalogue.json ../data/salesRecord.json 2>&1 | tee -a ../tests/bitacora_ejecucion.txt
#python3 computeSales.py ../data/priceCatalogue.json ../data/salesRecord_100k.json 2>&1 | tee -a ../tests/bitacora_ejecucion.txt
echo "" | tee -a ../tests/bitacora_ejecucion.txt

echo "===== $(date) =====" | tee -a ../tests/pylint_historial.txt
echo ">>> Ejecutando pylint..." | tee -a ../tests/pylint_historial.txt
pylint computeSales.py | tee -a ../tests/pylint_historial.txt
echo "" | tee -a ../tests/pylint_historial.txt

echo "===== $(date) =====" | tee -a ../tests/flake8_historial.txt
echo ">>> Ejecutando Flake8..." | tee -a ../tests/flake8_historial.txt
flake8 computeSales.py | tee -a ../tests/flake8_historial.txt
echo "" | tee -a ../tests/flake8_historial.txt