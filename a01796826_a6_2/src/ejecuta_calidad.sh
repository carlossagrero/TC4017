#!/bin/bash
#
# Script para ejecutar pruebas de calidad del código utilizando pylint y flake8
# Ubicación: src/ejecuta_calidad.sh

FECHA=$(date +%d/%m/%Y)
DIR_REPORTES="test_reports"
REPORTE="$DIR_REPORTES/test_report_calidad.txt"

mkdir -p "$DIR_REPORTES"

echo "------------------------------------------------------------" | tee -a "$REPORTE"
echo "****Prueba de Calidad ***** - $FECHA" | tee -a "$REPORTE"
echo "------------------------------------------------------------" | tee -a "$REPORTE"
echo "" | tee -a "$REPORTE"

echo "Ejecutando pylint..."
echo "------------------------------------------------------------" | tee -a "$REPORTE"
echo "Pylint Report - $FECHA" | tee -a "$REPORTE"
echo "------------------------------------------------------------" | tee -a "$REPORTE"
pylint src/ --output-format=text 2>&1 | tee -a "$REPORTE"

echo ""
echo "------------------------------------------------------------" | tee -a "$REPORTE"
echo "Flake8 Report - $FECHA" | tee -a "$REPORTE"
echo "------------------------------------------------------------" | tee -a "$REPORTE"
flake8 src/ --statistics 2>&1 | tee -a "$REPORTE"

echo "" | tee -a "$REPORTE"