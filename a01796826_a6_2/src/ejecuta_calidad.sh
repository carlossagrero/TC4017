#!/bin/bash
#
# Script para ejecutar pruebas de calidad del código utilizando pylint y flake8
# Ubicación: src/ejecuta_calidad.sh

FECHA=$(date +%d/%m/%Y)
DIR_REPORTES="test_reports"
REPORTE="$DIR_REPORTES/test_report_calidad.txt"

mkdir -p "$DIR_REPORTES"

echo "------------------------------------------------------------"
echo "Prueba de Calidad - $FECHA"
echo "------------------------------------------------------------"
echo ""

echo "Ejecutando pylint..."
echo "------------------------------------------------------------" | tee "$REPORTE"
echo "Pylint Report - $FECHA" | tee -a "$REPORTE"
echo "------------------------------------------------------------" | tee -a "$REPORTE"
pylint src/ --output-format=text | tee test_reports/test_report_calidad.txt | tee -a "$REPORTE"

echo ""
echo "------------------------------------------------------------" | tee -a "$REPORTE"
echo "Flake8 Report - $FECHA" | tee -a "$REPORTE"
echo "------------------------------------------------------------" | tee -a "$REPORTE"
flake8 src/ --statistics | tee test_reports/test_report_calidad.txt | tee -a "$REPORTE"

echo ""