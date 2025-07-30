import pandas as pd

def mostrar_matriz(df: pd.DataFrame) -> None:
    '''
    Muestra el contenido de un DataFrame con formato tabular.

    Args:
    1: df (pd.DataFrame): DataFrame con los Pokémon y sus atributos.

    Return:
    None (la función imprime por pantalla).
    '''
    print("\nID | Nombre       | Tipo       | Poder | Rareza")
    print("-" * 50)
    for _, fila in df.iterrows():
        print(f"{fila['id']:>3} | {fila['nombre']:<12} | {fila['tipo']:<10} | {fila['poder']:>5} | {fila['rareza']}")

def pokemons_sobre_promedio(df: pd.DataFrame) -> None:
    '''
    Calcula el promedio de poder y muestra los Pokémon que lo superan.

    Args:
    1: df (pd.DataFrame): DataFrame con los Pokémon y sus atributos.

    Return:
    None (la función imprime por pantalla).
    '''
    promedio = df['poder'].mean()
    filtrado = df[df['poder'] > promedio]
    print(f"\nPromedio de poder: {promedio:.2f}")
    mostrar_matriz(filtrado)

def trasponer_matriz(df: pd.DataFrame) -> None:
    '''
    Muestra la transposición del DataFrame (intercambia filas por columnas).

    Args:
    1: df (pd.DataFrame): DataFrame original.

    Return:
    None (la función imprime por pantalla).
    '''
    print("\nMatriz transpuesta:")
    print(df.T)
