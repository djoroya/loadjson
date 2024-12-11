import json
from  loadsavejson.listtonumpy import listtonumpy
from  loadsavejson.dicttopandas import dicttopandas,array2nplist


def loadjson(ruta_archivo):
    # Cargar el diccionario desde el archivo JSON
    with open(ruta_archivo, 'r') as archivo:
        diccionario = json.load(archivo)
    
    # Convertir listas en matrices de NumPy

    diccionario = listtonumpy(diccionario)
    diccionario = dicttopandas(diccionario)
    diccionario = array2nplist(diccionario)

    return diccionario


