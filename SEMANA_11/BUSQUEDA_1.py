# busqueda_matriz.py

def buscar_en_matriz(matriz, valor):
    """
    Busca un valor específico en una matriz bidimensional.

    :param matriz: Una lista de listas (matriz) con valores numéricos.
    :param valor: El valor a buscar en la matriz.
    :return: Una tupla con un booleano y una tupla de índices (fila, columna) si se encuentra el valor.
    """
    for i, fila in enumerate(matriz):
        for j, elem in enumerate(fila):
            if elem == valor:
                return True, (i, j)
    return False, None

def main():
    # Definir una matriz 3x3
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Valor a buscar
    valor_a_buscar = 3

    # Buscar el valor en la matriz
    encontrado, posicion = buscar_en_matriz(matriz, valor_a_buscar)

    # Mostrar el resultado
    if encontrado:
        print(f"El valor {valor_a_buscar} se encontró en la posición {posicion}.")
    else:
        print(f"El valor {valor_a_buscar} no se encontró en la matriz.")

if __name__ == "__main__":
    main()