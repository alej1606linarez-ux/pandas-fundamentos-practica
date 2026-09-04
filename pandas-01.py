import pandas as pd
import numpy as np

# df = pd.read_csv(r"C:\Users\Clark\OneDrive\Desktop\Coding\Python-aprendizaje\Fase 2 - Pandas\ventas.csv")

# # print(df.head(3))
# # print(df.describe())
# # df.info()

# norte = df[df["region"] == "Norte"]
# mayor_100 = df[df["monto"] > 100]
# print(norte)
# print(mayor_100)

# # Crear datos de ejemplo
# data = {"nombre": ["Ana", "Luis", "Carlos", "Marta"], "fruta": ["manzana", "pera", "platano", "manzana"]}
# df = pd.DataFrame(data)

# # Filtrar filas donde la fruta sea manzana o pera
# # resultado = df[df["fruta"].isin(["manzana", "pera"])]
# # print(resultado)

# resultado_excluido = df[~df["fruta"].isin(["manzana", "pera"])]
# print(resultado_excluido)

# 9/1/26 - Creacion de DataFrame para practicar con verbos fundamentales

import pandas as pd


# Tabla 1: transacciones de ventas
data_ventas = {
    'id_venta': range(1, 16),
    'fecha': pd.to_datetime(['2026-08-01','2026-08-02','2026-08-02','2026-08-03',
                              '2026-08-04','2026-08-05','2026-08-05','2026-08-06',
                              '2026-08-07','2026-08-08','2026-08-08','2026-08-09',
                              '2026-08-10','2026-08-10','2026-08-11']),
    'id_producto': [101,102,101,103,104,102,105,101,103,104,102,105,101,103,104],
    'cantidad': [3,1,5,2,np.nan,4,1,2,3,np.nan,2,6,1,4,3],
    'cliente': ['Ana Ruiz','Carlos Paz','Ana Ruiz','Beto Lima','Diana Vega',
                'Carlos Paz','Eva Soto','Ana Ruiz','Beto Lima','Diana Vega',
                'Carlos Paz','Eva Soto','Ana Ruiz','Beto Lima','Diana Vega'],
    'region': ['Norte','Sur','Norte','Centro','Sur','Sur','Norte','Norte',
               'Centro','Sur','Sur','Norte','Norte','Centro','Sur'],
    'metodo_pago': ['tarjeta','efectivo','tarjeta',np.nan,'tarjeta','tarjeta',
                     'efectivo','tarjeta',np.nan,'tarjeta','efectivo','tarjeta',
                     'tarjeta','efectivo',np.nan]
}
df_ventas = pd.DataFrame(data_ventas)

# Tabla 2: catálogo de productos
data_productos = {
    'id_producto': [101,102,103,104,105],
    'nombre_producto': ['Teclado','Mouse','Monitor','Audífonos','Webcam'],
    'categoria': ['Periféricos','Periféricos','Pantallas','Audio','Video'],
    'precio_unitario': [45000,20000,650000,80000,120000]
}
df_productos = pd.DataFrame(data_productos)

# Inicio de operación

# Prueba de que el codigo funciona
# print(df_ventas.head(5))
# print(df_productos.head(5))

# Imprimir selecciones + bool index + bool filter

# cliente = df_ventas[["cliente", "region", "cantidad"]]
# region = df_ventas["region"]
# cantidad = df_ventas["cantidad"]
# id_7 = df_ventas.loc[df_ventas["id_venta"] == 7]
# print(cliente)
# print(region)
# print(cantidad)
# print(id_7)

# ordenar

# menor_mayor = df_ventas.sort_values("cantidad")
# print(menor_mayor)

# mayor_menor = df_ventas.sort_values("cantidad", ascending= False)
# print(mayor_menor)

# dif_regs = df_ventas.sort_values(["region", "cantidad"], ascending= [True, False])
# print(dif_regs)

# buscar

# con_nombre = df_ventas[df_ventas["cliente"].str.contains("Eva Soto")]
# print(con_nombre)

# nombre_inc = df_ventas[df_ventas["cliente"].str.contains("Ana")]
# print(nombre_inc)

# doble = df_ventas[df_ventas["region"].isin(["Norte", "Sur"])]
# print(doble)

# Agrupar

# grupo_raw = df_ventas.groupby("region")
# print(grupo_raw)

# grupo_entero = df_ventas.groupby("region")["id_producto"].count()
# print(grupo_entero)

# cliente = df_ventas.groupby("cliente")["id_venta"].count()
# print(cliente)

# 9/2/26 - Agregar

# cantidades = df_ventas.groupby("region")["cantidad"].sum()
# print(cantidades)

# promedios = df_ventas.groupby("cliente")["cantidad"].mean()
# print(promedios)

# multiple = df_ventas.groupby("region")["cantidad"].agg(["sum", "mean", "max"])
# print(multiple)

# TRANSFORMAR

# df_ventas["cantidad_doble"] = df_ventas["cantidad"] * 2
# print(df_ventas["cantidad_doble"])

# df_ventas["cliente mayus"] = df_ventas["cliente"].str.upper()
# print(df_ventas["cliente mayus"])

# df_ventas["categoria_venta"] = np.where(df_ventas["cantidad"] >3, "alta", "baja")
# print(df_ventas["categoria_venta"])

# COMBINAR 

# prueba = df_ventas["id_producto"]
# print(prueba)

ventas_completas = pd.merge(df_ventas, df_productos, on="id_producto")
# # print(ventas_completas.head())

# ventas_completas["total_venta"] = ventas_completas["cantidad"] * ventas_completas["precio_unitario"]

# ventas_completas.groupby("categoria")["total_venta"].sum()

# print(ventas_completas.groupby("categoria")["total_venta"].sum())

faltantes = ventas_completas.isna().sum()

promedios = ventas_completas.copy()

promedios["cantidad"] = promedios["cantidad"].fillna(promedios["cantidad"].mean())

limpios = ventas_completas.dropna()

print(promedios)
