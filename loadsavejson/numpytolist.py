import numpy as np
def numpytolist(diccionario):
    diccionario = diccionario.copy()

    for clave, valor in diccionario.items():
        if isinstance(valor, np.ndarray):
            diccionario[clave] = valor.tolist()
        if isinstance(valor, dict): # if value is a dictionary
            diccionario[clave] = numpytolist(diccionario[clave])
        if isinstance(valor, list):
            # comprobar si es una lista de diccionarios
            bol = [isinstance(i,dict) for i in valor]
            bol = all(bol)
            if bol:
                for i in range(len(valor)):
                    valor[i] = numpytolist(valor[i])
            diccionario[clave] = valor
                    
    return diccionario
