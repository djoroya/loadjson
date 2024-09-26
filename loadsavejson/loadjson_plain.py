import json
def loadjson_plain(ruta_archivo):
    # Cargar el diccionario desde el archivo JSON
    with open(ruta_archivo, 'r') as archivo:
        diccionario = json.load(archivo)
    return diccionario