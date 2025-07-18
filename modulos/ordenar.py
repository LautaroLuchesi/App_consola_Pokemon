def comparar_y_ordenar(matriz: list[list], i: int):
    '''
    compara y orderna una fila con el resto segun vistas en DES

    args:
    1:matriz de datos
    2:i: indice de la fila actual

    return: none
    '''
    n = len(matriz)
    for j in range(i + 1, n):
            if float(matriz[i][1]) < float(matriz[j][1]):
                matriz[i], matriz[j] = matriz[j], matriz[i]

def ordenar_por_vistas(matriz: list[list]):
    '''
    ordena la matriz por vistas de forma descendente
    
    args: matriz de datos

    return: none
    '''
    n = len(matriz)
    for i in range(n - 1):
        comparar_y_ordenar(matriz, i)
    print("\n--- matriz ordenada por vistas(DES) ---")
    for fila in matriz:
        print(f"{fila[0]} | {fila[1]} | {fila[2]}")