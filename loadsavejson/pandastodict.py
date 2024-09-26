import pandas as pd

def pandastodict(diccionario):
    diccionario = diccionario.copy()

    for clave, valor in diccionario.items():
        if isinstance(valor, pd.DataFrame):
            keys   = valor.keys().tolist()
            values = valor.values.T.tolist()
            
            values = dict(zip(keys,values))
            values["pandas"] = None
            diccionario[clave] = values
        if isinstance(valor, dict): # if value is a dictionary
            diccionario[clave] = pandastodict(diccionario[clave])
    return diccionario