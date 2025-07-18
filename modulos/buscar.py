def cal_prom(matriz:list[list]):
    '''
    calcula el promedio de vistas y duraciones

    args:
    matriz: matriz de datos

    retutn: prom_vistas, prom_duracion
    '''
    total_vistas = 0
    total_duracion = 0
    cantidad = 0
    for fila in matriz:
        total_vistas += float(fila[1])
        total_duracion += float(fila[2])
        cantidad += 1
    
    prom_vistas = total_vistas / cantidad
    prom_duracion = total_duracion / cantidad
    return prom_vistas, prom_duracion

def buscar_superiores_prom(matriz:list[list]):
    '''
    busca y muestra los videos que superen el promedio de vistaqs y duracion

    args:
    matriz: matriz de datos

    return: none
    '''
    prom_vistas, prom_duracion = cal_prom(matriz)
    print("\nVideos con vistas y duracion mayores al promedio")
    for fila in matriz:
        if float(fila[1]) > prom_vistas and float(fila[2] > prom_duracion):
            print(f"{fila[0]} | {fila[1]} | {fila[2]}")

def filtrar_con_numeral(matriz: list[list]):
    '''
    filtra y muestra los videos que tienen un '#' en su nombre

    args:
    matriz: matriz de datos

    return : none
    '''
    print("\n--- videos con numeral en su nombre ---")
    for fila in matriz:
        if "#" in fila[0]:
            print(f"{fila[0]} | {fila[1]} | {fila[2]}")

