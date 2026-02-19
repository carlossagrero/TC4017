#!/bin/bash
set -euo pipefail

FECHA=$(date +%Y%m%d_%H%M%S)
DIR_REPORTES="test_reports"
REPORTE="$DIR_REPORTES/test_report_$FECHA.txt"

mkdir -p "$DIR_REPORTES"

pytest --cov=src.hotel --cov-report=term-missing -v | tee "$REPORTE"