# Función para mostrar la matriz completa con formato
def mostrar_matriz(df) -> None:
    print("\nID | Nombre       | Tipo       | Poder | Rareza")
    print("-" * 50)
    for _, fila in df.iterrows():
        print(f"{fila['id']:3} | {fila['nombre']:<12} | {fila['tipo']:<10} | {fila['poder']:5} | {fila['rareza']}")

# Función para mostrar Pokémon con poder superior al promedio
def pokemons_sobre_promedio(df) -> None:
    promedio = df['poder'].mean()
    filtrado = df[df['poder'] > promedio]
    print(f"\nPromedio de poder: {promedio:.2f}")
    mostrar_matriz(filtrado)

# Función para trasponer la matriz
def trasponer_matriz(df) -> None:
    print("\nMatriz transpuesta:")
    print(df.T)
