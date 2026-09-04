"""
Práctica de verbos fundamentales de Pandas
Verbos cubiertos: seleccionar, filtrar, ordenar, buscar, agrupar,
                   agregar, transformar, combinar, condicionar, manejar ausencia

Dataset de ejemplo: transacciones de ventas + catálogo de productos,
diseñado con nulos intencionales para practicar manejo de datos faltantes.
"""

import pandas as pd
import numpy as np

# ============================================
# CREACIÓN DEL DATASET DE PRÁCTICA
# ============================================

# Tabla 1: transacciones de ventas
data_ventas = {
    'id_venta': range(1, 16),
    'fecha': pd.to_datetime(['2026-08-01', '2026-08-02', '2026-08-02', '2026-08-03',
                              '2026-08-04', '2026-08-05', '2026-08-05', '2026-08-06',
                              '2026-08-07', '2026-08-08', '2026-08-08', '2026-08-09',
                              '2026-08-10', '2026-08-10', '2026-08-11']),
    'id_producto': [101, 102, 101, 103, 104, 102, 105, 101, 103, 104, 102, 105, 101, 103, 104],
    'cantidad': [3, 1, 5, 2, np.nan, 4, 1, 2, 3, np.nan, 2, 6, 1, 4, 3],
    'cliente': ['Ana Ruiz', 'Carlos Paz', 'Ana Ruiz', 'Beto Lima', 'Diana Vega',
                'Carlos Paz', 'Eva Soto', 'Ana Ruiz', 'Beto Lima', 'Diana Vega',
                'Carlos Paz', 'Eva Soto', 'Ana Ruiz', 'Beto Lima', 'Diana Vega'],
    'region': ['Norte', 'Sur', 'Norte', 'Centro', 'Sur', 'Sur', 'Norte', 'Norte',
               'Centro', 'Sur', 'Sur', 'Norte', 'Norte', 'Centro', 'Sur'],
    'metodo_pago': ['tarjeta', 'efectivo', 'tarjeta', np.nan, 'tarjeta', 'tarjeta',
                     'efectivo', 'tarjeta', np.nan, 'tarjeta', 'efectivo', 'tarjeta',
                     'tarjeta', 'efectivo', np.nan]
}
df_ventas = pd.DataFrame(data_ventas)

# Tabla 2: catálogo de productos
data_productos = {
    'id_producto': [101, 102, 103, 104, 105],
    'nombre_producto': ['Teclado', 'Mouse', 'Monitor', 'Audífonos', 'Webcam'],
    'categoria': ['Periféricos', 'Periféricos', 'Pantallas', 'Audio', 'Video'],
    'precio_unitario': [45000, 20000, 650000, 80000, 120000]
}
df_productos = pd.DataFrame(data_productos)

print("--- Vista inicial: df_ventas ---")
print(df_ventas.head())
print("\n--- Vista inicial: df_productos ---")
print(df_productos.head())


# ============================================
# VERBO: SELECCIONAR
# ============================================
# Selección de varias columnas a la vez (doble corchete) y de una fila
# específica filtrando por el valor real de la columna id_venta (no por
# posición del índice, que es un error común al confundir .loc con orden).

print("\n--- SELECCIONAR: columnas cliente, region, cantidad ---")
seleccion_columnas = df_ventas[["cliente", "region", "cantidad"]]
print(seleccion_columnas)

print("\n--- SELECCIONAR: fila donde id_venta == 7 ---")
fila_id_7 = df_ventas.loc[df_ventas["id_venta"] == 7]
print(fila_id_7)


# ============================================
# VERBO: ORDENAR
# ============================================

print("\n--- ORDENAR: cantidad ascendente ---")
orden_ascendente = df_ventas.sort_values("cantidad")
print(orden_ascendente)

print("\n--- ORDENAR: cantidad descendente ---")
orden_descendente = df_ventas.sort_values("cantidad", ascending=False)
print(orden_descendente)

print("\n--- ORDENAR: por region (asc) y luego cantidad (desc) ---")
orden_multiple = df_ventas.sort_values(["region", "cantidad"], ascending=[True, False])
print(orden_multiple)


# ============================================
# VERBO: BUSCAR
# ============================================
# .str.contains busca coincidencia parcial de texto; .isin busca
# coincidencia contra una lista de valores posibles.

print("\n--- BUSCAR: cliente que coincide con 'Eva Soto' ---")
busqueda_exacta = df_ventas[df_ventas["cliente"].str.contains("Eva Soto")]
print(busqueda_exacta)

print("\n--- BUSCAR: clientes que contienen 'Ana' ---")
busqueda_parcial = df_ventas[df_ventas["cliente"].str.contains("Ana")]
print(busqueda_parcial)

print("\n--- BUSCAR: region Norte o Sur ---")
busqueda_multiple = df_ventas[df_ventas["region"].isin(["Norte", "Sur"])]
print(busqueda_multiple)


# ============================================
# VERBO: AGRUPAR
# ============================================
# Agrupar por sí solo no genera un resultado imprimible directamente
# (es un objeto GroupBy); necesita una función de agregación después.

print("\n--- AGRUPAR: objeto GroupBy sin agregación (referencia en memoria) ---")
grupo_sin_agregar = df_ventas.groupby("region")
print(grupo_sin_agregar)

print("\n--- AGRUPAR + contar: filas por region, usando columna sin nulos ---")
conteo_por_region = df_ventas.groupby("region")["id_producto"].count()
print(conteo_por_region)

print("\n--- AGRUPAR + contar: ventas distintas por cliente ---")
conteo_por_cliente = df_ventas.groupby("cliente")["id_venta"].count()
print(conteo_por_cliente)


# ============================================
# VERBO: AGREGAR
# ============================================

print("\n--- AGREGAR: suma de cantidad por region ---")
suma_por_region = df_ventas.groupby("region")["cantidad"].sum()
print(suma_por_region)

print("\n--- AGREGAR: promedio de cantidad por cliente ---")
promedio_por_cliente = df_ventas.groupby("cliente")["cantidad"].mean()
print(promedio_por_cliente)

print("\n--- AGREGAR: suma, promedio y máximo a la vez, por region ---")
agregacion_multiple = df_ventas.groupby("region")["cantidad"].agg(["sum", "mean", "max"])
print(agregacion_multiple)


# ============================================
# VERBO: TRANSFORMAR + CONDICIONAR
# ============================================
# np.where cubre condiciones de 2 ramas; np.select cubre 3+ ramas,
# lo cual es necesario aquí para no perder la distinción de los NaN
# (con np.where, NaN > 3 se resuelve como False y se cuela como "baja").

df_ventas["cantidad_doble"] = df_ventas["cantidad"] * 2
df_ventas["cliente_mayus"] = df_ventas["cliente"].str.upper()

condiciones = [
    df_ventas["cantidad"].isna(),
    df_ventas["cantidad"] > 3,
    df_ventas["cantidad"] <= 3
]
resultados = ["sin dato", "alta", "baja"]
df_ventas["categoria_venta"] = np.select(condiciones, resultados, default="baja")

print("\n--- TRANSFORMAR + CONDICIONAR: columnas nuevas ---")
print(df_ventas[["cantidad", "cantidad_doble", "cliente_mayus", "categoria_venta"]])


# ============================================
# VERBO: COMBINAR
# ============================================
# merge cruza ambas tablas por la columna en común (id_producto).
# Por defecto es un inner join: solo trae filas que coinciden en ambas tablas.

ventas_completas = pd.merge(df_ventas, df_productos, on="id_producto")
ventas_completas["total_venta"] = ventas_completas["cantidad"] * ventas_completas["precio_unitario"]

print("\n--- COMBINAR: ventas + catálogo de productos ---")
print(ventas_completas.head())

print("\n--- COMBINAR + AGREGAR: total vendido por categoría de producto ---")
total_por_categoria = ventas_completas.groupby("categoria")["total_venta"].sum()
print(total_por_categoria)


# ============================================
# VERBO: MANEJAR AUSENCIA
# ============================================
# Tres estrategias distintas frente a los mismos nulos:
# 1. Solo contarlos (diagnóstico).
# 2. Rellenarlos con el promedio (conserva todas las filas, introduce un sesgo).
# 3. Eliminar las filas con cualquier nulo (pierde filas, no distorsiona con estimaciones).

print("\n--- MANEJAR AUSENCIA: conteo de nulos por columna ---")
conteo_nulos = ventas_completas.isna().sum()
print(conteo_nulos)

print("\n--- MANEJAR AUSENCIA: cantidad rellenada con el promedio ---")
ventas_rellenas = ventas_completas.copy()
ventas_rellenas["cantidad"] = ventas_rellenas["cantidad"].fillna(ventas_rellenas["cantidad"].mean())
print(ventas_rellenas[["cliente", "cantidad"]])

print("\n--- MANEJAR AUSENCIA: filas con cualquier nulo eliminadas ---")
ventas_sin_nulos = ventas_completas.dropna()
print(ventas_sin_nulos[["cliente", "cantidad", "metodo_pago"]])
