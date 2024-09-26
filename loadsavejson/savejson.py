from loadsavejson.numpytolist import numpytolist
from loadsavejson.pandastodict import pandastodict
import json
import numpy as np

def savejson(diccionario, ruta_archivo):
    diccionario = diccionario.copy()
    # 
    # diccionario: diccionario a guardar
    assert isinstance(diccionario, dict), "El diccionario debe ser un diccionario de Python"
    # ruta_archivo: ruta del archivo JSON
    assert isinstance(ruta_archivo, str), "La ruta del archivo debe ser un string"
    
    # Convertir matrices de NumPy en listas
    # copy dictionary
    diccionario = numpytolist(diccionario)
    diccionario = pandastodict(diccionario)

    
    #comprobar que los valores son de tipo nativo no numpy
    for clave, valor in diccionario.items():
        if type(valor) == np.int64:
            diccionario[clave] = int(valor)


    # Guardar el diccionario en un archivo JSON
    with open(ruta_archivo, 'w') as archivo:
        # pretty print
        json.dump(diccionario, archivo, indent=4)