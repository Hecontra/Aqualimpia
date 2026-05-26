import pandas as pd
from joblib import dump


def exportar_excel(df, ruta_salida):
    """
    Exporta un DataFrame a archivo Excel.
    """
    df.to_excel(ruta_salida, index=False)


def guardar_resultados_joblib(resultados, ruta_salida):
    """
    Guarda resultados del análisis en formato joblib para reutilizarlos.
    """
    dump(resultados, ruta_salida)


def generar_reporte_resumen(df, ruta_salida):
    """
    Genera un reporte Excel con resumen estadístico básico.
    """
    resumen = df.describe()
    resumen.to_excel(ruta_salida)
