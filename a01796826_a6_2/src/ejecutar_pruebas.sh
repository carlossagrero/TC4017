#!/bin/bash
set -euo pipefail

FECHA=$(date +%d/%m/%Y)
DIR_REPORTES="test_reports"
REPORTE="$DIR_REPORTES/test_report_log.txt"
AWK_COVERAGE='/^=+ tests coverage =+/ {show=1} show {print} /^=+ [0-9]+ (passed|failed|error|errors|skipped).* =+/ {if (show) {show=0}}'


echo "============================================================" >> "$REPORTE"
echo "Reporte de pruebas - $FECHA" >> "$REPORTE"
echo "============================================================" >> "$REPORTE"
echo "" >> "$REPORTE"
echo "[TEST] hotel.py" >> "$REPORTE"
echo "------------------------------------------------------------" >> "$REPORTE"
pytest tests/test_hotel.py --cov=src.hotel --cov-report=term-missing -v 2>&1 \
	| tee -a "$REPORTE" \
	| awk "$AWK_COVERAGE"; printf "\n\n"
echo "" >> "$REPORTE"

echo "[TEST] hotel_service.py" >> "$REPORTE"
echo "------------------------------------------------------------" >> "$REPORTE"
pytest tests/test_hotel_service.py --cov=src.hotel_service --cov-report=term-missing -v 2>&1 \
	| tee -a "$REPORTE" \
	| awk "$AWK_COVERAGE"; printf "\n\n"
echo "" >> "$REPORTE"

echo "[TEST] customer.py" >> "$REPORTE"
echo "------------------------------------------------------------" >> "$REPORTE"
pytest tests/test_customer.py --cov=src.customer --cov-report=term-missing -v 2>&1 \
	| tee -a "$REPORTE" \
	| awk "$AWK_COVERAGE"; printf "\n\n"
echo "" >> "$REPORTE"

echo "[TEST] customer_service.py" >> "$REPORTE"
echo "------------------------------------------------------------" >> "$REPORTE"
pytest tests/test_customer_service.py --cov=src.customer_service --cov-report=term-missing -v 2>&1 \
	| tee -a "$REPORTE" \
	| awk "$AWK_COVERAGE"; printf "\n\n"
echo "" >> "$REPORTE"

echo "[TEST] reservation.py" >> "$REPORTE"
echo "------------------------------------------------------------" >> "$REPORTE"
pytest tests/test_reservation.py --cov=src.reservation --cov-report=term-missing -v 2>&1 \
	| tee -a "$REPORTE" \
	| awk "$AWK_COVERAGE"; printf "\n\n"
echo "" >> "$REPORTE"

echo "[TEST] reservation_service.py" >> "$REPORTE"
echo "------------------------------------------------------------" >> "$REPORTE"
pytest tests/test_reservation_service.py --cov=src.reservation_service --cov-report=term-missing -v 2>&1 \
	| tee -a "$REPORTE" \
	| awk "$AWK_COVERAGE"; printf "\n\n"
echo "" >> "$REPORTE"