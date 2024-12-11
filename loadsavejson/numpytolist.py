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
            
            # comprobar si es una lista de numpy arrays
            bol_numpy = [isinstance(i,np.ndarray) for i in valor]
            bol_numpy = all(bol_numpy)

            if bol:
                for i in range(len(valor)):
                    valor[i] = numpytolist(valor[i])

            if bol_numpy:
                for i in range(len(valor)):
                    valor[i] = valor[i].tolist()
                
                valor = {"numpy_list": None, "list": valor}

            diccionario[clave] = valor
                    
    return diccionario
