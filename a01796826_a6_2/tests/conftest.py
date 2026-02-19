import sys
from pathlib import Path

# Agrega el directorio raíz al path para que pytest encuentre el módulo src
sys.path.insert(0, str(Path(__file__).parent.parent))
