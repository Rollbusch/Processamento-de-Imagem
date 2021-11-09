import numpy as np


def imagem_to_cinza(matrix_colorida: np.array) -> np.array:
    linhas = matrix_colorida.shape[0]
    colunas = matrix_colorida.shape[1]

    matrix_gray = np.zeros((linhas, colunas))

    for i in range(linhas):
        for j in range(colunas):
            r, g, b = matrix_colorida[i, j]
            matrix_gray[i, j] = int((r + g + b) / 3)

    return matrix_gray

def imagem_rgb(matrix_colorida: np.array) -> np.array:
    linhas = matrix_colorida.shape[0]
    colunas = matrix_colorida.shape[1]

    matrix_rgb = []
    matriz_r = np.zeros((linhas, colunas))
    matriz_g = np.zeros((linhas, colunas))
    matriz_b = np.zeros((linhas, colunas))

    for i in range(linhas):
        for j in range(colunas):
            r, g, b = matrix_colorida[i, j]
            matriz_r[i, j] = int(r)
            matriz_g[i, j] = int(g)
            matriz_b[i, j] = int(b)
    matrix_rgb.append(matriz_r)
    matrix_rgb.append(matriz_g)
    matrix_rgb.append(matriz_b)
    return matrix_rgb


