import pandas as pd
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
