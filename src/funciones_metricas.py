import pandas as pd


def resumen_numerico(df):
    """
    Genera un resumen estadístico de las variables numéricas.
    """
    return df.describe()


def promedio_por_planta(df, columna_grupo, columna_valor):
    """
    Calcula el promedio de una variable numérica agrupada por planta u otra categoría.
    """
    resumen = df.groupby(columna_grupo)[columna_valor].mean().reset_index()
    return resumen


def calcular_correlaciones(df):
    """
    Calcula la matriz de correlación solo para variables numéricas.
    """
    numericas = df.select_dtypes(include=["int64", "float64"])
    return numericas.corr()
