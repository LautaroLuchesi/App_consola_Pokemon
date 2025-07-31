import pandas as pd
import modificaciones as mod
import matriz as mat

df = pd.read_csv("archivos/pokemons.csv")

def menu() -> None:
    '''
    Muestra un menú interactivo en consola para ejecutar diferentes operaciones sobre el DataFrame de Pokémon.
    Permite al usuario seleccionar opciones para mostrar datos, filtrar, ordenar y salir del programa.

    Args:
    No recibe argumentos.

    Return:
    None (la función controla el flujo del programa y muestra resultados en consola).
    '''
    while True:
        print("\n--- Menú de Opciones ---")
        print("1. Mostrar matriz")
        print("2. Mostrar Pokémon con poder superior al promedio")
        print("3. Ordenar legendarios por poder (desc)")
        print("4. Filtrar por tipo 'fuego'")
        print("5. Trasponer matriz")
        print("6. Mostrar Pokemon mas fuerte por tipo")
        print("7. Salir")
        opcion = mod.validar_opcion("Elige una opcion entre 1 y 7: ", 1, 7)

        match opcion:
            case 1 :
                mat.mostrar_matriz(df)
            case 2:
                mat.pokemons_sobre_promedio(df)
            case 3:
                mod.ordenar_legendarios(df)
            case 4:
                mod.filtrar_fuego(df)
            case 5:
                mat.trasponer_matriz(df)
            case 6:
                mod.mas_fuerte_por_tipo(df)
            case 7:
                print("Saliendo del programa...")
                break

menu()
