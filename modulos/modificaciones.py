import pandas as pd
import modulos.matriz as mat

def validar_opcion(mensaje: str, val_min: int, val_max: int) -> int:
    '''
    valida que el usuario ingrese una opcion valida mediante recursion

    arg:
    1:mensaje: mensasje que se muestra
    2:val_min: valor minimo valido
    3:val_max: valor maximo valido

    retun:
    opcion valida ingresada
    '''
    entrada = input(mensaje)
    if not entrada.isdigit():
        print("Se debe ingresar un numero")
        return validar_opcion(mensaje, val_min, val_max)
    entrada = int(entrada)
    if entrada < val_min or entrada > val_max:
        print("Opcion fuera del rango")
        return validar_opcion(mensaje, val_min, val_max)
    return entrada

def ordenar_legendarios(df: pd.DataFrame) -> None:
    '''
    Filtra los Pokémon legendarios y los ordena por poder de mayor a menor, luego muestra la matriz.

    Args:
    1: df (DataFrame): DataFrame que contiene los Pokémon con sus atributos.

    Return:
    None (la función no retorna nada, solo muestra los datos por pantalla).
    '''
    legendarios = df[df['rareza'].str.lower() == 'legendario']
    ordenados = legendarios.sort_values(by='poder', ascending=False)
    mat.mostrar_matriz(ordenados)

def filtrar_fuego(df: pd.DataFrame) -> None:
    '''
    Filtra los Pokémon de tipo fuego y muestra la matriz con los resultados.

    Args:
    1: df (DataFrame): DataFrame que contiene los Pokémon con sus atributos.

    Return:
    None (la función no retorna nada, solo muestra los datos por pantalla).
    '''
    fuego = df[df['tipo'].str.lower() == 'fuego']
    mat.mostrar_matriz(fuego)

