import pandas as pd


def revisar_valores_nulos(df):
    """
    Revisa la cantidad de valores nulos por columna.
    """
    nulos = df.isnull().sum().reset_index()
    nulos.columns = ["columna", "valores_nulos"]
    return nulos


def revisar_duplicados(df):
    """
    Calcula la cantidad de registros duplicados.
    """
    return df.duplicated().sum()


def revisar_calidad_general(df):
    """
    Entrega una revisión básica de calidad de datos.
    """
    resultado = {
        "filas": df.shape[0],
        "columnas": df.shape[1],
        "duplicados": df.duplicated().sum(),
        "valores_nulos_totales": df.isnull().sum().sum()
    }

    return resultado
