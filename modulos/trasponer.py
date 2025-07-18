def copiar_columna(matriz: list[list], indice: int) -> list[list]:
    '''
    copia una columna de la matriz

    args:
    1: matriz de datos
    2:indice de la columna

    return:
    nueva fila (columna transpuesta)
    '''
    nueva_fila = []
    for fila in matriz:
        nueva_fila.append(fila[indice])
    return nueva_fila
    
def trasponer_matriz(matriz: list[list]):
    '''
    transforma fila en columnas y muestra la matriz transpuesta

    args:
    matriz de datos

    return: none
    '''
    print("\n--- matriz traspuesta ---")
    columnas = len(matriz[0]) if matriz else 0
    traspuesta = []
    for i in range(columnas):
        fila_transpuesta = copiar_columna(matriz, i)
        traspuesta.append(fila_transpuesta)
    for fila in traspuesta:
        print(fila)