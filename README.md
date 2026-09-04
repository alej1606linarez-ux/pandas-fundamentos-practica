# Práctica de fundamentos de Pandas

Bitácora de práctica enfocada en dominar los verbos fundamentales de Pandas, como parte de mi transición hacia un rol de Data Analyst. Este no es un proyecto de análisis con conclusiones de negocio (ese vive en un repositorio aparte) — es evidencia del proceso de aprendizaje y dominio técnico de la sintaxis y lógica de Pandas.

## Contexto

Vengo de una base de fundamentos de Python (variables, condicionales, ciclos, funciones, manejo de archivos) y de un primer proyecto de fundamentos puro (simulador de ATM, sin librerías externas). Este repositorio documenta el siguiente paso: aprender Pandas a través de la práctica deliberada de los verbos que son transferibles entre Pandas, SQL y Excel — la lógica es la misma, solo cambia la sintaxis según la herramienta.

## Verbos cubiertos

| Verbo | Qué practica |
|---|---|
| Seleccionar | Elegir columnas específicas y filas por condición (no por posición de índice) |
| Filtrar | Boolean indexing como base de toda selección condicional |
| Ordenar | `sort_values` simple y con múltiples columnas/direcciones |
| Buscar | Coincidencia exacta y parcial de texto (`.str.contains`), coincidencia contra lista de valores (`.isin`) |
| Agrupar | `groupby` como paso de preparación, distinto de la agregación en sí |
| Agregar | Funciones de resumen (`sum`, `mean`, `count`) individuales y combinadas (`.agg()`) |
| Transformar | Creación de columnas nuevas a partir de operaciones sobre columnas existentes |
| Condicionar | `np.where` (2 ramas) vs `np.select` (3+ ramas), y por qué importa la diferencia al tratar con nulos |
| Combinar | `merge` de dos tablas relacionadas por una clave en común |
| Manejar ausencia | Diagnóstico de nulos, relleno con `fillna()`, eliminación con `dropna()`, y el trade-off entre ambos |

## Dataset

Dataset sintético de dos tablas relacionadas (transacciones de ventas y catálogo de productos), diseñado intencionalmente con valores nulos en las columnas `cantidad` y `metodo_pago` para poder practicar manejo de datos faltantes de forma controlada.

## Cómo correrlo

```bash
pip install pandas numpy
python pandas_fundamentos.py
```

El script imprime el resultado de cada verbo por separado, con etiquetas descriptivas en consola.

## Próximo paso

Aplicar estos mismos verbos sobre un dataset real de gran volumen (~180K filas) en un proyecto de análisis con preguntas de negocio concretas — ver repositorio de proyecto de portafolio.
