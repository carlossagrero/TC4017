#!/bin/bash
#
# Script para ejecutar la aplicación de escritorio del sistema de hoteles
# Ubicación: src/ejecutar_app.sh

# Ir al directorio padre (raíz del proyecto)
cd "$(dirname "$0")/.."

# Activar entorno si existe
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi

# Ejecutar la aplicación
python3 -m src.app_desktop
