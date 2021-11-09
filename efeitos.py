import sys
import os
sys.path.insert(0, os.path.join('..', 'srcs'))

import utils.imagens_files as imfi
import utils.imagens_transformacoes as transformacoes
import numpy as np

def blur(arquivo):
    # Convertendo a imagem para uma matriz
    matriz_colorida = imfi.file_to_matriz(arquivo)
    matriz_rgb = transformacoes.imagem_rgb(matriz_colorida)

    # Pegando as 3 cores separadas (r, g, b)
    matriz_imagem_r = matriz_rgb[0].copy()
    matriz_imagem_g = matriz_rgb[1].copy()
    matriz_imagem_b = matriz_rgb[2].copy()

    # Todas as 3 cores tem os mesmos tamanhos entao eu
    # pego a cor R para setar a linha e coluna
    lins = matriz_imagem_r.shape[0]
    cols = matriz_imagem_r.shape[1]

    m = matriz_imagem_r
    for i in range(1, lins - 1):
        for j in range(1, cols - 1):
            matriz_imagem_r[i][j] = (
                                            1 * m[i - 1][j - 1] + 1 * m[i - 1][j] + 1 * m[i - 1][j + 1] +
                                            1 * m[i][j - 1] + 1 * m[i][j] + 1 * m[i][j + 1] +
                                            1 * m[i + 1][j - 1] + 1 * m[i + 1][j] + 1 * m[i + 1][j + 1]
                                    ) / 9
            matriz_imagem_r[i][j] = max(0, matriz_imagem_r[i][j])
            matriz_imagem_r[i][j] = min(255, matriz_imagem_r[i][j])

    m = matriz_imagem_g
    for i in range(1, lins - 1):
        for j in range(1, cols - 1):
            matriz_imagem_g[i][j] = (
                                            1 * m[i - 1][j - 1] + 1 * m[i - 1][j] + 1 * m[i - 1][j + 1] +
                                            1 * m[i][j - 1] + 1 * m[i][j] + 1 * m[i][j + 1] +
                                            1 * m[i + 1][j - 1] + 1 * m[i + 1][j] + 1 * m[i + 1][j + 1]
                                    ) / 9
            matriz_imagem_g[i][j] = max(0, matriz_imagem_g[i][j])
            matriz_imagem_g[i][j] = min(255, matriz_imagem_g[i][j])

    m = matriz_imagem_b
    for i in range(1, lins - 1):
        for j in range(1, cols - 1):
            matriz_imagem_b[i][j] = (
                                            1 * m[i - 1][j - 1] + 1 * m[i - 1][j] + 1 * m[i - 1][j + 1] +
                                            1 * m[i][j - 1] + 1 * m[i][j] + 1 * m[i][j + 1] +
                                            1 * m[i + 1][j - 1] + 1 * m[i + 1][j] + 1 * m[i + 1][j + 1]
                                    ) / 9
            matriz_imagem_b[i][j] = max(0, matriz_imagem_b[i][j])
            matriz_imagem_b[i][j] = min(255, matriz_imagem_b[i][j])

    tamanho_lin = matriz_imagem_r.shape[0]
    tamanho_col = matriz_imagem_r.shape[1]

    nova_imagem = []

    for i in range(1, tamanho_lin):
        nova_linha = []
        for j in range(1, tamanho_col):
            nova_linha.append([int(matriz_imagem_r[i][j]), int(matriz_imagem_g[i][j]), int(matriz_imagem_b[i][j])])
        nova_imagem.append(nova_linha)

    nova_imagem = np.array(nova_imagem, np.int32)

    return nova_imagem

def sobel(arquivo):
    # Convertendo a imagem para uma matriz
    matriz_colorida = imfi.file_to_matriz(arquivo)
    matriz_cinza = transformacoes.imagem_to_cinza(matriz_colorida)


    # Todas as 3 cores tem os mesmos tamanhos entao eu
    # pego a cor R para setar a linha e coluna
    lins = matriz_cinza.shape[0]
    cols = matriz_cinza.shape[1]

    matriz_imagem_sobel_vertical = matriz_cinza.copy()
    matriz_imagem_sobel_horizontal = matriz_cinza.copy()

    m = matriz_cinza
    for i in range(1, lins - 1):
        for j in range(1, cols - 1):
            matriz_imagem_sobel_vertical[i][j] = (
                    1 * m[i - 1][j - 1] + 0 * m[i - 1][j] + -1 * m[i - 1][j + 1] +
                    2 * m[i][j - 1] + 0 * m[i][j] + -2 * m[i][j + 1] +
                    1 * m[i + 1][j - 1] + 0 * m[i + 1][j] + -1 * m[i + 1][j + 1]
            )
            matriz_imagem_sobel_vertical[i][j] = max(0, matriz_imagem_sobel_vertical[i][j])
            matriz_imagem_sobel_vertical[i][j] = min(255, matriz_imagem_sobel_vertical[i][j])

    m = matriz_cinza
    for i in range(1, lins - 1):
        for j in range(1, cols - 1):
            matriz_imagem_sobel_horizontal[i][j] = (
                    1 * m[i - 1][j - 1] + 2 * m[i - 1][j] + 1 * m[i - 1][j + 1] +
                    0 * m[i][j - 1] + 0 * m[i][j] + 0 * m[i][j + 1] +
                    -1 * m[i + 1][j - 1] + -2 * m[i + 1][j] + -1 * m[i + 1][j + 1]
            )
            matriz_imagem_sobel_horizontal[i][j] = max(0, matriz_imagem_sobel_horizontal[i][j])
            matriz_imagem_sobel_horizontal[i][j] = min(255, matriz_imagem_sobel_horizontal[i][j])

    matriz_imagem_sobel = matriz_imagem_sobel_horizontal + matriz_imagem_sobel_vertical
    for i in range(1, lins - 1):
        for j in range(1, cols - 1):
            matriz_imagem_sobel[i][j] = max(0, matriz_imagem_sobel[i][j])
            matriz_imagem_sobel[i][j] = min(255, matriz_imagem_sobel[i][j])

    return matriz_imagem_sobel

def unsharp(arquivo):
    # Convertendo a imagem para uma matriz
    imagem_original = imfi.file_to_matriz(arquivo)
    imagem_blured = blur(arquivo)

    lins = imagem_original.shape[0]
    cols = imagem_original.shape[1]
    cores = imagem_original.shape[2]

    imagem_unsharpened = np.zeros((lins + 1, cols + 1, cores))
    pixel_sub = np.zeros((lins + 1, cols + 1, cores))

    for i in range(0, lins - 1):
        for j in range(0, cols - 1):
            for cor in range(0, cores):
                pixel_sub[i][j][cor] = imagem_original[i][j][cor] - imagem_blured[i][j][cor]
                imagem_unsharpened[i][j][cor] = max(0, pixel_sub[i][j][cor])

    return np.array(imagem_unsharpened, np.uint8)

def sharpening(arquivo):
    # pegando imagem unsharped
    imagem_unshaped = unsharp(arquivo)

    # Convertendo a imagem para uma matriz
    imagem_original = imfi.file_to_matriz(arquivo)

    lins = imagem_original.shape[0]
    cols = imagem_original.shape[1]
    cores = imagem_original.shape[2]

    imagem_sharpening = np.zeros((lins, cols, cores))
    pixel_add = np.zeros((lins, cols, cores))

    for i in range(0, lins):
        for j in range(0, cols):
            for cor in range(0, cores):
                pixel_add[i][j][cor] = imagem_original[i][j][cor] + imagem_unshaped[i][j][cor]
                imagem_sharpening[i][j][cor] = min(255, pixel_add[i][j][cor])

    return np.array(imagem_sharpening, np.uint8)
