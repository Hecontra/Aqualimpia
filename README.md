# Proyecto de Ciencia de Datos - AquaLimpia S. A.

## 1. Descripción del proyecto

AquaLimpia S. A. es una empresa dedicada al tratamiento de aguas residuales urbanas e industriales. Durante el último trimestre se han identificado incumplimientos intermitentes en parámetros críticos de calidad del efluente, principalmente en la DBO de salida y en la eficiencia del tratamiento.

El presente proyecto aplica un análisis exploratorio de datos para evaluar el desempeño operativo y ambiental de las plantas de tratamiento, con el fin de apoyar la toma de decisiones de las áreas de Operaciones y Gestión Ambiental.

---

## 2. Objetivo general

Analizar el desempeño de las plantas de tratamiento de AquaLimpia S. A. mediante un flujo de trabajo reproducible, que permita identificar patrones asociados al caudal de entrada, carga contaminante, DBO de salida, eficiencia de tratamiento y cumplimiento normativo.

---

## 3. Objetivos específicos

- Cargar y revisar el dataset oficial `dataset_set_A_aguas_residuales.xlsx`.
- Evaluar la calidad inicial de los datos, considerando valores nulos, duplicados y tipos de variables.
- Calcular indicadores operacionales y ambientales, como eficiencia de remoción de DBO y porcentaje de cumplimiento normativo.
- Construir un dashboard exploratorio para comparar el desempeño de las plantas.
- Generar archivos de salida diferenciados para el Área de Operaciones y el Área de Gestión Ambiental.
- Documentar el proceso para facilitar su revisión, reproducción y actualización futura.

---

## 4. Preguntas de análisis

- ¿Qué plantas presentan mayores niveles promedio de DBO de salida?
- ¿Qué porcentaje de cumplimiento normativo presenta cada planta?
- ¿Existe relación visual entre el caudal de entrada y la DBO de salida?
- ¿Qué plantas requieren mayor atención desde el punto de vista operativo o ambiental?
- ¿Qué limitaciones presentan los datos utilizados para apoyar decisiones?

---

## 5. Dataset utilizado

El archivo utilizado corresponde a:

`dataset_set_A_aguas_residuales.xlsx`

El dataset contiene 200 registros y 10 columnas:

| Columna | Descripción |
|---|---|
| fecha_registro | Fecha del registro operacional |
| planta | Planta de tratamiento evaluada |
| caudal_entrada_m3_d | Caudal de entrada en metros cúbicos por día |
| DBO_entrada_mg_L | DBO del agua residual antes del tratamiento |
| SST_entrada_mg_L | Sólidos suspendidos totales de entrada |
| pH_entrada | Nivel de pH de entrada |
| energia_aeracion_kWh | Consumo energético del proceso de aireación |
| lodos_generados_kg_d | Cantidad de lodos generados por día |
| DBO_salida_mg_L | DBO del efluente tratado |
| cumplimiento_norma | Estado de cumplimiento normativo, donde 1 = cumple y 0 = no cumple |

---

## 6. Herramientas utilizadas

El análisis fue desarrollado en Python, utilizando las siguientes librerías:

- `pandas`: carga, limpieza y manipulación de datos.
- `numpy`: cálculos numéricos.
- `matplotlib`: visualización básica.
- `seaborn`: gráficos estadísticos exploratorios.
- `plotly`: construcción de dashboard interactivo.
- `joblib`: almacenamiento de resultados reutilizables.
- `openpyxl`: lectura y exportación de archivos Excel.

---

## 7. Metodología aplicada

El flujo de análisis se desarrolló en las siguientes etapas:

1. **Carga del dataset**
   - Se importó el archivo Excel oficial del caso.
   - Se revisaron las primeras filas, columnas y dimensiones del dataset.

2. **Revisión de calidad de datos**
   - Se verificó la existencia de valores nulos.
   - Se revisaron registros duplicados.
   - Se analizaron los tipos de datos y las estadísticas descriptivas.

3. **Preparación de indicadores**
   - Se convirtió la fecha de registro a formato fecha.
   - Se calculó la eficiencia de remoción de DBO.
   - Se creó una etiqueta textual para el cumplimiento normativo.

4. **Análisis exploratorio**
   - Se agruparon los datos por planta.
   - Se calcularon promedios de caudal, DBO de entrada, DBO de salida, energía, lodos y cumplimiento normativo.

5. **Construcción del dashboard**
   - Se generaron visualizaciones comparativas para evaluar:
     - DBO de salida promedio por planta.
     - Eficiencia promedio de remoción de DBO.
     - Relación entre caudal de entrada y DBO de salida.
     - Porcentaje de cumplimiento normativo por planta.

6. **Generación de reportes**
   - Se creó un archivo para el Área de Operaciones.
   - Se creó un archivo para el Área de Gestión Ambiental.

7. **Documentación y publicación**
   - Se documentó el análisis en el notebook.
   - Se creó este archivo `README.md`.
   - Se organizó el proyecto para ser publicado en GitHub.

---

## 8. Archivos generados

| Archivo | Descripción |
|---|---|
| `analisis_aqualimpia.ipynb` | Notebook principal del análisis |
| `dataset_set_A_aguas_residuales.xlsx` | Dataset oficial utilizado |
| `reporte_operaciones.xlsx` | Reporte para el Área de Operaciones |
| `reporte_gestion_ambiental.xlsx` | Reporte para el Área de Gestión Ambiental |
| `dashboard_aqualimpia.html` | Dashboard exploratorio interactivo |
| `resultados_aqualimpia.joblib` | Resultados reutilizables del análisis |
| `README.md` | Documentación técnica del proyecto |

---

## 9. Resultados principales

A partir del análisis inicial del dataset se identificó lo siguiente:

- El dataset contiene 200 registros.
- No se detectaron valores nulos.
- No se detectaron registros duplicados.
- Las plantas analizadas son:
  - Planta Sur
  - Planta Norte
  - Planta Centro
- La variable `cumplimiento_norma` permite identificar si un registro cumple o no con la normativa ambiental.
- Se observaron más registros de incumplimiento que de cumplimiento, lo que indica la necesidad de revisar con mayor detalle el desempeño ambiental de las plantas.

El análisis por planta permite comparar el comportamiento de la DBO de salida, la eficiencia de tratamiento y el porcentaje de cumplimiento normativo. Estos resultados permiten priorizar acciones correctivas y apoyar reportes ambientales con evidencia analítica.

---

## 10. Interpretación general

El dashboard exploratorio muestra que el desempeño de las plantas no debe evaluarse mediante una sola variable. La DBO de salida permite observar la calidad del efluente tratado, mientras que la eficiencia de remoción de DBO permite evaluar qué tan efectivo fue el proceso respecto de la carga contaminante inicial.

La relación entre caudal de entrada y DBO de salida permite explorar si mayores volúmenes de ingreso podrían asociarse con dificultades operacionales. Además, el porcentaje de cumplimiento normativo por planta ayuda a identificar posibles riesgos regulatorios y a orientar acciones preventivas.

---

## 11. Limitaciones del análisis

- El análisis es exploratorio, por lo que no permite establecer causalidad directa.
- El dataset corresponde a un período determinado, por lo que los resultados podrían variar con nuevos registros.
- La variable `cumplimiento_norma` resume el cumplimiento como 0 o 1, pero no entrega detalle sobre la causa específica del incumplimiento.
- No se incluyen variables externas como clima, mantenciones, fallas de equipos o cambios operativos.
- Las conclusiones deben interpretarse considerando el contexto operacional y ambiental de cada planta.

---

## 12. Consideraciones éticas

Los resultados del análisis pueden influir en decisiones operacionales, inversiones, priorización de plantas y reportes ambientales. Por ello, deben comunicarse de manera responsable, evitando conclusiones simplistas o afirmaciones que no estén respaldadas por los datos.

La información debe utilizarse para apoyar mejoras en los procesos de tratamiento y cumplimiento ambiental, no para atribuir responsabilidades sin un análisis técnico más profundo.

---

## 13. Conclusión

La documentación técnica permite comprender el desarrollo completo del proyecto, desde la carga del dataset hasta la generación de dashboards y reportes. En el caso de AquaLimpia S. A., esta documentación facilita la reproducción del análisis, la revisión por otros integrantes del equipo y la continuidad del trabajo en futuros períodos.

El proyecto permite transformar datos operacionales y ambientales en información útil para la toma de decisiones, apoyando tanto al Área de Operaciones como al Área de Gestión Ambiental.

