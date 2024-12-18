# JSON Handling with NumPy and Pandas Support

Este proyecto proporciona funciones para guardar y cargar diccionarios que contienen matrices de **NumPy** y **DataFrames de Pandas** en archivos JSON, manejando correctamente las conversiones entre estos tipos de datos y los tipos nativos de Python.

## Funcionalidades

1. **Guardar diccionarios en formato JSON**:
   - Convierte matrices de NumPy a listas.
   - Convierte DataFrames de Pandas a diccionarios anidados.
   - Guarda el diccionario convertido en un archivo JSON con formato legible (indentación).
   
2. **Cargar diccionarios desde archivos JSON**:
   - Carga el diccionario desde el archivo JSON.
   - Convierte listas en matrices de NumPy.
   - Convierte los diccionarios anidados en DataFrames de Pandas.

## Instalación

Asegúrate de tener instaladas las siguientes dependencias en tu entorno de Python:

```bash
pip install numpy pandas
``` 

## Uso
1. Guardar un diccionario en un archivo JSON:
python
Copiar código
from your_module import savejson

## Ejemplo de diccionario que contiene matrices de NumPy y DataFrames de Pandas

```python
diccionario = {
    "matriz_numpy": np.array([[1, 2], [3, 4]]),
    "dataframe_pandas": pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
}
```

Guardar el diccionario en un archivo JSON
```python
savejson(diccionario, 'archivo.json')
```

# Cargar el diccionario desde un archivo JSON
diccionario_cargado = loadjson('archivo.json')
3. Funciones disponibles
* savejson(diccionario, ruta_archivo): Guarda un diccionario en un archivo JSON. Convierte matrices de NumPy y DataFrames de Pandas a tipos nativos de Python (listas y diccionarios, respectivamente) antes de guardar.

* loadjson(ruta_archivo): Carga un diccionario desde un archivo JSON. Convierte listas a matrices de NumPy y diccionarios anidados a DataFrames de Pandas cuando es necesario.

* numpytolist(diccionario): Convierte todas las matrices de NumPy en listas dentro de un diccionario.

* pandastodict(diccionario): Convierte DataFrames de Pandas a diccionarios anidados.

* dicttopandas(diccionario): Convierte diccionarios anidados en DataFrames de Pandas.

* listtonumpy(diccionario): Convierte listas en matrices de NumPy cuando es posible.

# Ejemplos
Guardar y Cargar un Diccionario con NumPy y Pandas:
```python	
import numpy as np
import pandas as pd
from your_module import savejson, loadjson

# Crear diccionario con NumPy y Pandas

data = {
    "numeros": np.array([1, 2, 3]),
    "tabla": pd.DataFrame({"A": [1, 2], "B": [3, 4]})
}

# Guardar el diccionario
savejson(data, 'datos.json')

# Cargar el diccionario
data_cargado = loadjson('datos.json')

print(data_cargado)
```

