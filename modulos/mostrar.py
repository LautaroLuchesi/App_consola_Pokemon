def mostrar_matriz(matriz: list[list]):
    '''
    muestra la informacion de cada fila de la matriz con un formato especifico
    
    args:
    matriz: la matriz de datos
    
    returns: none
    '''
    print("\n--- Datos de videos ---")
    for fila in matriz:
        print(f"{fila[0]} | {fila[1]} | {fila[2]}")


