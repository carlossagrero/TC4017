#!/bin/bash

echo "===== $(date) =====" | tee -a ../tests/pylint_historial.txt

echo ">>> Ejecutando programa Python..." | tee -a ../tests/pylint_historial.txt
python3 convertNumbers.py fileWithData.txt | tee -a ../tests/pylint_historial.txt

echo "" | tee -a ../tests/pylint_historial.txt
echo ">>> Ejecutando pylint..." | tee -a ../tests/pylint_historial.txt
pylint convertNumbers.py | tee -a ../tests/pylint_historial.txt

echo "" | tee -a ../tests/pylint_historial.txt