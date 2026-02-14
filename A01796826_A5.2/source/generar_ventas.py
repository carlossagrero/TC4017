import json
import random
from pathlib import Path

CATALOGO = Path("../data/priceCatalogue.json")
SALIDA = Path("../data/salesRecord_100k.json")

TOTAL_RENGLONES = 100_000
MAX_ITEMS_POR_VENTA = 5

def main():
    productos = json.loads(CATALOGO.read_text(encoding="utf-8"))
    nombres = [p["title"] for p in productos]

    registros = []
    sale_id = 1
    usados = 0

    while usados < TOTAL_RENGLONES:
        items_venta = random.randint(1, MAX_ITEMS_POR_VENTA)
        for _ in range(items_venta):
            if usados >= TOTAL_RENGLONES:
                break
            registros.append(
                {
                    "SALE_ID": sale_id,
                    "Product": random.choice(nombres),
                    "Quantity": random.randint(1, 10),
                }
            )
            usados += 1
        sale_id += 1

    SALIDA.write_text(
        json.dumps(registros, indent=2),
        encoding="utf-8"
    )

    print(f"Archivo generado: {SALIDA}")
    print(f"Ventas: {sale_id - 1}")
    print(f"Renglones: {len(registros)}")

if __name__ == "__main__":
    main()