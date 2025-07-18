from utn_fra.datasets import (
    lista_bzrp_nombres,
    lista_bzrp_vistas,
    lista_bzrp_duracion
)
from modulos.crear import crear_matriz
from modulos.mostrar import mostrar_matriz
from modulos.validaciones import validar_opcion
from modulos.buscar import buscar_superiores_prom, filtrar_con_numeral
from modulos.ordenar import ordenar_por_vistas
from modulos.trasponer import trasponer_matriz
def main():
    matriz = crear_matriz(lista_bzrp_nombres, lista_bzrp_vistas, lista_bzrp_duracion)
    while True:
        print("--- MENU DE OPCIONES ---")
        print("1. Mostrar datos")
        print("2. Buscar datos mayores al promedio (vistas y duracion)")
        print("3. Ordenar datos por vistas (DES)")
        print("4. Filtrar datos (nombre con '#')")
        print("5. Trasponer datos")
        print("Salir")

        opcion = validar_opcion("Elige una opcion entre 1 y 6: ", 1, 6)
        match opcion:
            case 1:
                if matriz :
                    mostrar_matriz(matriz)
                else :
                    print("La matriz esta vacia")
            case 2:
                if matriz :
                    buscar_superiores_prom(matriz)
                else :
                    print("La matriz esta vacia")
            case 3:
                if matriz:
                    ordenar_por_vistas(matriz)
                else :
                    print("La matriz esta vacia")
            case 4:
                if matriz : 
                    filtrar_con_numeral(matriz)
                else:
                    print("La matriz esta vacia")
            case 5:
                if matriz : 
                    trasponer_matriz(matriz)
                else:
                    print("La matriz esta vacia")
            case 6:
                print("Saliendo del programa...")
                break

main()