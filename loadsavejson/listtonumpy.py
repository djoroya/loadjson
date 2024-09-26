import numpy as np
def listtonumpy(diccionario):
    diccionario = diccionario.copy()
    for clave, valor in diccionario.items():
        if isinstance(valor, list):
            try:
                diccionario[clave] = np.array(valor)
            except:
                # comprobar si es una lista de diccionarios
                bol = [isinstance(i,dict) for i in valor]
                bol = all(bol)
                if bol:
                    for i in range(len(valor)):
                        valor[i] = listtonumpy(valor[i])
                    diccionario[clave] = valor
                else:
                    print("Error en la clave: ", clave)
                    diccionario[clave] = valor
        if isinstance(valor, dict): # if value is a dictionary
            diccionario[clave] = listtonumpy(diccionario[clave])
            
    return diccionario