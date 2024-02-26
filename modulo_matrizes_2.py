diagonais_primas = []

for tamanho_matriz in range(3,4):

    # generator numeros
    # num = (n for n in range(1,t**3*2,2))
    num = (n for n in range(1, tamanho_matriz**3+1))

    # formação matriz

    matriz_list = list()
    linhas_list = list()
    colunas_list = list()
        
    for matriz in range(tamanho_matriz):
        for linha in range(tamanho_matriz):
            for coluna in range(tamanho_matriz):
                colunas_list.append(next(num))
            linhas_list.append(colunas_list[:])
            colunas_list.clear()
        matriz_list.append(linhas_list[:])
        linhas_list.clear()

    maior = len(str(matriz_list[-1][-1][-1]))

    diagonais_iniciais = [
        (lin,col,cam)
        for cam in range(tamanho_matriz)
        for lin in range(tamanho_matriz)
        for col in range(tamanho_matriz)
        if cam == 0
    ]

    todas_as_diagonais_list = [[],[],[],[]]

    for diagonal_n in todas_as_diagonais_list:
        for coodenada in diagonais_iniciais:
                diagonal_temporaria = []
                z = coodenada[0]
                y = coodenada[1]
                x = coodenada[2]
                for k in range(tamanho_matriz):
                    diagonal_temporaria.append(matriz_list[z][y][x])
                    if z == tamanho_matriz-1:
                        diagonal_n.append(diagonal_temporaria)
                    if diagonal_n == todas_as_diagonais_list[0]:
                        z += 1
                        y += 1
                        x += 1
                        if z > tamanho_matriz-1:
                            z = 0
                        if y > tamanho_matriz-1:
                            y = 0
                        if x > tamanho_matriz-1:
                            x = 0
                    elif diagonal_n == todas_as_diagonais_list[1]:
                        z += 1
                        y += -1
                        x += 1
                        if z > tamanho_matriz-1:
                            z = 0
                        if y < 0:
                            y = tamanho_matriz-1
                        if x > tamanho_matriz-1:
                            x = 0
                    elif diagonal_n == todas_as_diagonais_list[2]:
                        z += 1
                        y += -1
                        x += -1
                        if z > tamanho_matriz-1:
                            z = 0
                        if y < 0:
                            y = tamanho_matriz-1
                        if x < 0:
                            x = tamanho_matriz-1
                    elif diagonal_n == todas_as_diagonais_list[3]:
                        z += 1
                        y += 1
                        x += -1
                        if z > tamanho_matriz-1:
                            z = 0
                        if y > tamanho_matriz-1:
                            y = 0
                        if x < 0:
                            x = tamanho_matriz-1
        for diagonal_n in todas_as_diagonais_list:
            diagonal_n.sort()
            for cada_valor in diagonal_n:
                cada_valor.sort()

    # print(todas_as_diagonais_list[0])

    exibicao = todas_as_diagonais_list[0]

    for cordenada in exibicao:
        print(cordenada)
    print()

    # print('Diagonais primas: ',diagonais_primas)



