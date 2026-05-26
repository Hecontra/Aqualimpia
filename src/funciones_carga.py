import pandas as pd


def cargar_datos(ruta_archivo):
    """
    Carga el dataset desde un archivo Excel.

    Parámetros:
    ruta_archivo: ruta del archivo Excel.

    Retorna:
    DataFrame con los datos cargados.
    """
    df = pd.read_excel(ruta_archivo)
    return df


def mostrar_resumen_inicial(df):
    """
    Muestra información básica del dataset.
    """
    print("Primeras filas del dataset:")
    print(df.head())

    print("\nCantidad de filas y columnas:")
    print(df.shape)

    print("\nColumnas disponibles:")
    print(df.columns.tolist())

    print("\nTipos de datos:")
    print(df.dtypes)
