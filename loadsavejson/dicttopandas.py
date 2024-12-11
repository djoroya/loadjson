import pandas as pd
import numpy as np
def dicttopandas(diccionario):
    diccionario = diccionario.copy()

    for clave, valor in diccionario.items():
        if isinstance(valor, dict):
            if "pandas" in valor.keys():
                valor.pop("pandas")
                valor = pd.DataFrame(valor)
                diccionario[clave] = valor
        if isinstance(valor, dict): # if value is a dictionary
            diccionario[clave] = dicttopandas(diccionario[clave])
    return diccionario


def array2nplist(diccionario):
    diccionario = diccionario.copy()

    for clave, valor in diccionario.items():
        if isinstance(valor, dict):
            if "numpy_list" in valor.keys():
                valor.pop("numpy_list")
                valor =  [np.array(i) for i in valor["list"]]
                diccionario[clave] = valor
        if isinstance(valor, dict): # if value is a dictionary
            diccionario[clave] = array2nplist(diccionario[clave])
    return diccionario
