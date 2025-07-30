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

# Función para ordenar legendarios por poder DESC
def ordenar_legendarios(df):
    legendarios = df[df['rareza'].str.lower() == 'legendario']
    ordenados = legendarios.sort_values(by='poder', ascending=False)
    mat.mostrar_matriz(ordenados)

# Función para filtrar por tipo fuego
def filtrar_fuego(df):
    fuego = df[df['tipo'].str.lower() == 'fuego']
    mat.mostrar_matriz(fuego)
