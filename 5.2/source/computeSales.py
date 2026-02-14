#!/usr/bin/env python3
"""
computeSales.py

Uso:
    python computeSales.py priceCatalogue.json salesRecord.json

Requisitos cubiertos:
- Lee 2 archivos JSON desde línea de comandos.
- Calcula el costo total de todas las ventas usando el catálogo de precios.
- Imprime resultados en pantalla y los guarda en SalesResults.txt (legible para humanos).
- Maneja datos inválidos: reporta errores y continúa.
- Escala a cientos/miles de ítems.
- Mide e incluye tiempo transcurrido.
- Cumple PEP8 y usa nombres en español.
"""
# pylint: disable=invalid-name
from __future__ import annotations

import json
import sys
import time
from dataclasses import dataclass, field
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


ARCHIVO_SALIDA = "../results/SalesResults.txt"
MONEDA = "USD"
REDONDEO = Decimal("0.01")


@dataclass(frozen=True)
class ErrorDato:
    contexto: str
    detalle: str


@dataclass
class ResumenProceso:
    total_ventas: int = 0
    total_renglones: int = 0
    total_items: int = 0

    errores_catalogo: int = 0
    errores_ventas: int = 0

    items_sin_precio: int = 0
    cantidad_invalida: int = 0

    detalles_errores: List[str] = field(default_factory=list)
    max_detalles_errores: int = 200  # límite para no llenar el archivo y se vea feo


def imprimir_error(mensaje: str) -> None:
    print(f"[ERROR] {mensaje}", file=sys.stderr)

def registrar_error(resumen: ResumenProceso, mensaje: str) -> None:
    resumen.errores_ventas += 1
    imprimir_error(mensaje)
    if len(resumen.detalles_errores) < resumen.max_detalles_errores:
        resumen.detalles_errores.append(mensaje)

def registrar_advertencia(resumen: ResumenProceso, mensaje: str) -> None:
    imprimir_advertencia(mensaje)
    if len(resumen.detalles_errores) < resumen.max_detalles_errores:
        resumen.detalles_errores.append("[ADVERTENCIA] " + mensaje)


def imprimir_advertencia(mensaje: str) -> None:
    print(f"[ADVERTENCIA] {mensaje}", file=sys.stderr)


def leer_json_desde_archivo(ruta: Path) -> Optional[Any]:
    try:
        contenido = ruta.read_text(encoding="utf-8")
    except OSError as exc:
        imprimir_error(f"No se pudo leer el archivo '{ruta}': {exc}")
        return None

    try:
        return json.loads(contenido)
    except json.JSONDecodeError as exc:
        imprimir_error(f"JSON inválido en '{ruta}': {exc}")
        return None


def normalizar_texto(valor: Any) -> Optional[str]:
    if isinstance(valor, str):
        texto = valor.strip()
        return texto if texto else None
    return None


def convertir_a_decimal(valor: Any) -> Optional[Decimal]:
    """
    Convierte a Decimal valores típicos (int, float, str numérico).
    Si es inválido, regresa None.
    """
    if isinstance(valor, (int, float, str)):
        try:
            # str() para evitar problemas de representación float
            return Decimal(str(valor))
        except (InvalidOperation, ValueError):
            return None
    return None


def obtener_lista_ventas(datos_ventas: Any) -> Tuple[List[Any], List[ErrorDato]]:
    """
    Acepta formatos:
    - Lista de ventas: [...]
    - Dict con llave: {"sales":[...]} / {"ventas":[...]} ...
    - Lista plana de renglones (tu caso):
      [{"SALE_ID":1,"Product":"X","Quantity":2,...}, ...]
      Se agrupa por SALE_ID (y por SALE_Date si existe) para formar ventas con 'items'.
    """
    errores: List[ErrorDato] = []

    def es_renglon_plano(obj: Any) -> bool:
        if not isinstance(obj, dict):
            return False
        return (
            "Product" in obj and "Quantity" in obj and ("SALE_ID" in obj or "sale_id" in obj)
            and not any(k in obj for k in ("items", "products", "productos", "details", "detalles"))
        )

    def agrupar_renglones(renglones: List[dict]) -> List[dict]:
        grupos: Dict[Tuple[Any, Any], List[dict]] = {}
        for idx, r in enumerate(renglones):
            sale_id = r.get("SALE_ID", r.get("sale_id"))
            sale_date = r.get("SALE_Date", r.get("sale_date"))
            if sale_id is None:
                errores.append(
                    ErrorDato(contexto=f"ventas[{idx}]", 
                              detalle="Falta SALE_ID; no se puede agrupar.")
                )
                # Lo metemos como venta individual
                key = (f"sin_id_{idx}", sale_date)
            else:
                key = (sale_id, sale_date)

            grupos.setdefault(key, []).append(r)

        ventas_agrupadas: List[dict] = []
        for (sale_id, sale_date), rows in grupos.items():
            items = []
            for r in rows:
                items.append(
                    {
                        "product": r.get("Product"),
                        "quantity": r.get("Quantity"),
                    }
                )
            ventas_agrupadas.append(
                {
                    "sale_id": sale_id,
                    "sale_date": sale_date,
                    "items": items,
                }
            )
        # Orden estable por sale_id (si es comparable)
        try:
            ventas_agrupadas.sort(key=lambda v: (str(v.get("sale_id")), str(v.get("sale_date"))))
        except Exception:
            pass
        return ventas_agrupadas

    # 1) Lista directa
    if isinstance(datos_ventas, list):
        if datos_ventas and all(es_renglon_plano(x) for x in datos_ventas):
            return agrupar_renglones(datos_ventas), errores
        return datos_ventas, errores

    # 2) Dict con llave conocida
    if isinstance(datos_ventas, dict):
        for llave in ("sales", "ventas", "records", "registro", "data"):
            posible = datos_ventas.get(llave)
            if isinstance(posible, list):
                if posible and all(es_renglon_plano(x) for x in posible):
                    return agrupar_renglones(posible), errores
                return posible, errores

        errores.append(
            ErrorDato(
                contexto="ventas",
                detalle=(
                    "Estructura no reconocida: se esperaba una lista o una "
                    "llave como 'sales'/'ventas' con una lista."
                ),
            )
        )
        return [], errores

    errores.append(
        ErrorDato(
            contexto="ventas",
            detalle="Tipo inválido: se esperaba una lista o un objeto JSON.",
        )
    )
    return [], errores

def construir_catalogo_precios(
    datos_catalogo: Any,
) -> Tuple[Dict[str, Decimal], List[ErrorDato]]:
    """
    Construye un dict: {nombre_producto: precio_decimal}
    Soporta estos formatos comunes:
    - Lista de objetos: [{"title":"A","price": 10}, ...]
      o [{"product":"A","price": 10}, ...]
      o [{"name":"A","price": 10}, ...]
    - Dict directo: {"A": 10, "B": 5.5}
    - Dict con lista: {"catalogue":[...]} o {"catalog":[...]} o {"products":[...]}
    """
    errores: List[ErrorDato] = []
    catalogo: Dict[str, Decimal] = {}

    def registrar_item(nombre: Any, precio: Any, idx: str) -> None:
        nombre_norm = normalizar_texto(nombre)
        if not nombre_norm:
            errores.append(
                ErrorDato(
                    contexto=f"catálogo[{idx}]",
                    detalle="Nombre de producto ausente o inválido.",
                )
            )
            return

        precio_dec = convertir_a_decimal(precio)
        if precio_dec is None:
            errores.append(
                ErrorDato(
                    contexto=f"catálogo[{idx}]",
                    detalle=f"Precio inválido para '{nombre_norm}': {precio!r}",
                )
            )
            return

        if precio_dec < 0:
            errores.append(
                ErrorDato(
                    contexto=f"catálogo[{idx}]",
                    detalle=f"Precio negativo para '{nombre_norm}': {precio_dec}",
                )
            )
            return

        catalogo[nombre_norm] = precio_dec

    if isinstance(datos_catalogo, dict):
        # Caso 1: dict directo { "A": 10, "B": 5 }
        # Si parece ser dict de precios (valores escalares numéricos)
        if all(
            isinstance(k, str) and isinstance(v, (int, float, str))
            for k, v in datos_catalogo.items()
        ):
            for k, v in datos_catalogo.items():
                registrar_item(k, v, k)
            return catalogo, errores

        # Caso 2: dict con lista en una llave conocida
        for llave in ("catalogue", "catalog", "products", "productos", "items"):
            posible = datos_catalogo.get(llave)
            if isinstance(posible, list):
                datos_catalogo = posible
                break

    if isinstance(datos_catalogo, list):
        for i, item in enumerate(datos_catalogo):
            idx = str(i)
            if not isinstance(item, dict):
                errores.append(
                    ErrorDato(
                        contexto=f"catálogo[{idx}]",
                        detalle=f"Se esperaba un objeto, se recibió: {type(item).__name__}",
                    )
                )
                continue

            nombre = (
                item.get("title")
                or item.get("product")
                or item.get("name")
                or item.get("producto")
                or item.get("nombre")
            )
            precio = item.get("price") or item.get("precio") or item.get("cost")
            registrar_item(nombre, precio, idx)

        return catalogo, errores

    errores.append(
        ErrorDato(
            contexto="catálogo",
            detalle=(
                "Estructura no reconocida: se esperaba lista, dict directo "
                "de precios, o un dict con una llave tipo 'catalogue/products'."
            ),
        )
    )
    return {}, errores


def extraer_items_de_venta(
    venta: Any,
    indice: int,
) -> Tuple[List[Tuple[Optional[str], Optional[Decimal]]], List[ErrorDato]]:
    """
    Extrae items como lista de (nombre_producto, cantidad_decimal).

    Soporta formatos comunes por venta:
    - {"items":[{"product":"A","quantity":2}, ...]}
    - {"items":{"A":2,"B":1}}
    - {"products":[...]} o {"productos":[...]} o {"details":[...]}
    """
    errores: List[ErrorDato] = []
    items: List[Tuple[Optional[str], Optional[Decimal]]] = []

    if not isinstance(venta, dict):
        errores.append(
            ErrorDato(
                contexto=f"venta[{indice}]",
                detalle=f"Se esperaba un objeto, se recibió: {type(venta).__name__}",
            )
        )
        return items, errores

    contenedor = None
    for llave in ("items", "products", "productos", "details", "detalles"):
        if llave in venta:
            contenedor = venta.get(llave)
            break

    if contenedor is None:
        errores.append(
            ErrorDato(
                contexto=f"venta[{indice}]",
                detalle="No se encontró lista/dict de items (keys esperadas: items/products/...).",
            )
        )
        return items, errores

    # Formato dict: {"A":2,"B":1}
    if isinstance(contenedor, dict):
        for nombre, cantidad in contenedor.items():
            nombre_norm = normalizar_texto(nombre)
            cantidad_dec = convertir_a_decimal(cantidad)
            items.append((nombre_norm, cantidad_dec))
        return items, errores

    # Formato lista: [{"product":"A","quantity":2}, ...]
    if isinstance(contenedor, list):
        for j, item in enumerate(contenedor):
            if not isinstance(item, dict):
                errores.append(
                    ErrorDato(
                        contexto=f"venta[{indice}].item[{j}]",
                        detalle=f"Se esperaba un objeto, se recibió: {type(item).__name__}",
                    )
                )
                items.append((None, None))
                continue

            nombre = (
                item.get("product")
                or item.get("title")
                or item.get("name")
                or item.get("producto")
                or item.get("nombre")
            )
            cantidad = (
                item.get("quantity")
                or item.get("qty")
                or item.get("cantidad")
                or item.get("count")
            )

            nombre_norm = normalizar_texto(nombre)
            cantidad_dec = convertir_a_decimal(cantidad)
            items.append((nombre_norm, cantidad_dec))

        return items, errores

    errores.append(
        ErrorDato(
            contexto=f"venta[{indice}]",
            detalle=f"Items con tipo inválido: {type(contenedor).__name__}",
        )
    )
    return items, errores


def formatear_moneda(monto: Decimal, moneda: str = MONEDA) -> str:
    monto_red = monto.quantize(REDONDEO, rounding=ROUND_HALF_UP)
    # Formato con separador de miles (estilo anglosajón); legible y estándar.
    return f"{moneda} {monto_red:,.2f}"


def calcular_totales(
    catalogo: Dict[str, Decimal],
    ventas: List[Any],
) -> Tuple[Decimal, List[str], ResumenProceso]:
    """
    Retorna:
    - total_general
    - lineas_detalle (human readable)
    - resumen (contadores y métricas)
    """
    resumen = ResumenProceso(total_ventas=len(ventas))
    total_general = Decimal("0")
    lineas: List[str] = []

    encabezado = (
        "RESULTADOS DE VENTAS\n"
        "====================\n"
        f"Moneda: {MONEDA}\n"
        f"Ventas procesadas: {len(ventas)}\n"
    )
    lineas.append(encabezado)

    # Guardamos temporalmente las líneas de ventas para agregarlas al final
    lineas_ventas: List[str] = []

    for i, venta in enumerate(ventas, start=1):
        items, errores_items = extraer_items_de_venta(venta, i)

        # Registrar errores de estructura
        for err in errores_items:
            registrar_error(resumen, f"{err.contexto}: {err.detalle}")

        subtotal = Decimal("0")
        conteo_items_validos = 0

        # Encabezado por venta
        lineas_ventas.append(f"\nVenta # {i:04d}")
        lineas_ventas.append("-" * 40)

        for j, (nombre_producto, cantidad) in enumerate(items, start=1):
            resumen.total_items += 1

            if not nombre_producto:
                registrar_error(resumen, f"venta[{i}] item[{j}]: nombre inválido/ausente.")
                continue

            if cantidad is None:
                resumen.cantidad_invalida += 1
                registrar_error(
                    resumen,
                    f"venta[{i}] item[{j}]: cantidad inválida para '{nombre_producto}'."
                )
                continue

            # Regla: no permitir cero (pero permitir negativos si son devoluciones)
            if cantidad == 0:
                resumen.cantidad_invalida += 1
                registrar_error(
                    resumen,
                    f"venta[{i}] item[{j}]: cantidad cero para '{nombre_producto}'."
                )
                continue

            precio = catalogo.get(nombre_producto)
            if precio is None:
                resumen.items_sin_precio += 1
                registrar_advertencia(
                    resumen,
                    f"venta[{i}] item[{j}]: producto '{nombre_producto}' no existe en catálogo.\n"
                    f"Se omite del cálculo."
                )
                continue

            total_item = precio * cantidad
            subtotal += total_item
            conteo_items_validos += 1

            lineas_ventas.append(
                f"- {nombre_producto} | qty={cantidad} | unit={formatear_moneda(precio)} | "
                f"total={formatear_moneda(total_item)}"
            )

        total_general += subtotal
        resumen.total_renglones += 1

        lineas_ventas.append(f"Subtotal venta # {i:04d}: {formatear_moneda(subtotal)}")
        lineas_ventas.append(f"Items válidos: {conteo_items_validos}")

    # -------------------------
    # RESUMEN (al inicio)
    # -------------------------
    resumen_lineas = [
        "\nRESUMEN\n-------",
        f"Total general: {formatear_moneda(total_general)}",
        f"Errores en catálogo: {resumen.errores_catalogo}",
        f"Errores en ventas:   {resumen.errores_ventas}",
        f"Items sin precio:    {resumen.items_sin_precio}",
        f"Cantidad inválida:   {resumen.cantidad_invalida}",
    ]

    # -------------------------
    # DETALLE DE ERRORES (después del resumen)
    # -------------------------
    detalle_errores_lineas = [
        "\nDETALLE DE ERRORES (muestra)",
        "---------------------------",
    ]

    if resumen.detalles_errores:
        for msg in resumen.detalles_errores:
            detalle_errores_lineas.append(f"- {msg}")

        if resumen.errores_ventas > len(resumen.detalles_errores):
            detalle_errores_lineas.append(
                f"- ... ({resumen.errores_ventas - len(resumen.detalles_errores)} errores adicionales no mostrados)"
            )
    else:
        detalle_errores_lineas.append("Sin errores reportados.")

    # Construcción final del reporte:
    # Encabezado (lineas[0]) + Resumen + Detalle errores + Ventas
    lineas[1:1] = resumen_lineas + detalle_errores_lineas
    lineas.extend(lineas_ventas)

    return total_general, lineas, resumen

def escribir_resultados(ruta_salida: Path, lineas: Iterable[str]) -> None:
    try:
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)
        ruta_salida.write_text(
            "\n".join(lineas) + "\n",
            encoding="utf-8",
            newline="\n"
        )
    except OSError as exc:
        imprimir_error(f"No se pudo escribir '{ruta_salida}': {exc}")


def imprimir_uso() -> None:
    print(
        "Uso:\n"
        "  python computeSales.py priceCatalogue.json salesRecord.json\n",
        file=sys.stderr,
    )


def main(argv: List[str]) -> int:
    if len(argv) != 3:
        imprimir_uso()
        return 2

    ruta_catalogo = Path(argv[1])
    ruta_ventas = Path(argv[2])

    inicio = time.perf_counter()

    datos_catalogo = leer_json_desde_archivo(ruta_catalogo)
    datos_ventas = leer_json_desde_archivo(ruta_ventas)

    if datos_catalogo is None or datos_ventas is None:
        imprimir_error("No se pudo continuar por errores críticos de lectura/parseo.")
        return 1

    catalogo, errores_cat = construir_catalogo_precios(datos_catalogo)
    resumen_cat = len(errores_cat)
    for err in errores_cat:
        imprimir_error(f"{err.contexto}: {err.detalle}")

    ventas, errores_ventas_estructura = obtener_lista_ventas(datos_ventas)
    for err in errores_ventas_estructura:
        imprimir_error(f"{err.contexto}: {err.detalle}")

    total, lineas, resumen = calcular_totales(catalogo, ventas)

    # Contabilizar errores de catálogo y de estructura (si aplican)
    resumen.errores_catalogo += resumen_cat
    for _ in errores_ventas_estructura:
        resumen.errores_ventas += 1

    # Medir tiempo transcurrido
    fin = time.perf_counter()
    tiempo_transcurrido = Decimal(str(fin - inicio))

    # Bloque TIEMPO (para insertarlo al inicio del reporte)
    bloque_tiempo = [
        "\nTIEMPO\n------",
        f"Tiempo transcurrido: {tiempo_transcurrido.quantize(REDONDEO)} s",
    ]

    # Insertar TIEMPO justo después del encabezado
    lineas[1:1] = bloque_tiempo

    # Salida en pantalla (human readable)
    print("\n".join(lineas))

    # Salida en archivo
    escribir_resultados(Path(ARCHIVO_SALIDA), lineas)

    # Exit code: 0 aunque haya errores de datos (Req3: continuar ejecución)
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
