
def crear_matriz(nombres: list, vistas: list, duraciones: list) -> list[list]:
    '''
    crea una matriz a partir de las listas de nombres, vistas y duraciones.

    args:
    1:nombres: Lista de nombres de los videos
    2:vistas: lista de vistas
    3:duraciones:lista de duracion de cada video

    returns:
    list: matriz con sublistas de [nombre, vistas, duracion]
    '''
    matriz = []
    for i in range(len(nombres)):
        fila = [nombres[i], vistas[i], duraciones[i]]
        matriz.append(fila)
    return matriz

