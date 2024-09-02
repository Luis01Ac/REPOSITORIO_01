# ordenar_fila_matriz.py

def quicksort(arr):
    """
    Ordena una lista utilizando el algoritmo de ordenación QuickSort.

    :param arr: Lista de números a ordenar.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def ordenar_fila(matriz, fila):
    """
    Ordena una fila específica de una matriz en orden ascendente usando QuickSort.

    :param matriz: Lista de listas (matriz) con valores numéricos.
    :param fila: Índice de la fila a ordenar.
    """
    matriz[fila] = quicksort(matriz[fila])


def mostrar_matriz(matriz):
    """
    Muestra una matriz en formato de filas y columnas.

    :param matriz: Lista de listas que representa la matriz.
    """
    for fila in matriz:
        print(fila)
    print()


def main():
    # Definir una matriz 4x4
    matriz = [
        [12, 5, 7, 3],
        [6, 14, 11, 9],
        [10, 1, 8, 2],
        [15, 4, 13, 16]
    ]

    # Mostrar la matriz original
    print("Matriz original:")
    mostrar_matriz(matriz)

    # Fila a ordenar (índice basado en cero)
    fila_a_ordenar = 2

    # Ordenar la fila específica usando QuickSort
    ordenar_fila(matriz, fila_a_ordenar)

    # Mostrar la matriz con la fila ordenada
    print("Matriz con la fila ordenada:")
    mostrar_matriz(matriz)


if __name__ == "__main__":
    main()