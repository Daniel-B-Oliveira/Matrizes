diagonais_primas = []
for t in range(2,4):

    # generator numeros
    # num = (n for n in range(1,t**3*2,2))
    num = (n for n in range(t**3))

    # formação matriz

    matriz_list = list()
    linhas_list = list()
    colunas_list = list()
        
    for c1 in range(t):
        for c2 in range(t):
            for c3 in range(t):
                colunas_list.append(next(num))
            linhas_list.append(colunas_list[:])
            colunas_list.clear()
        matriz_list.append(linhas_list[:])
        linhas_list.clear()

    maior = len(str(matriz_list[-1][-1][-1]))

    diagonais_iniciais = [
        (lin,col,cam)
        for cam in range(t)
        for lin in range(t)
        for col in range(t)
        if cam == 0
    ]



    todas_as_diagonais_list = [[],[],[],[]]

    for diagonal_n in todas_as_diagonais_list:
        for coodenada in diagonais_iniciais:
                diagonal_temporaria = []
                z = coodenada[0]
                y = coodenada[1]
                x = coodenada[2]
                for k in range(t):
                    diagonal_temporaria.append(matriz_list[z][y][x])
                    if z == t-1:
                        diagonal_n.append(diagonal_temporaria)
                    if diagonal_n == todas_as_diagonais_list[0]:
                        z += 1
                        y += 1
                        x += 1
                        if z > t-1:
                            z = 0
                        if y > t-1:
                            y = 0
                        if x > t-1:
                            x = 0
                    elif diagonal_n == todas_as_diagonais_list[1]:
                        z += 1
                        y += -1
                        x += 1
                        if z > t-1:
                            z = 0
                        if y < 0:
                            y = t-1
                        if x > t-1:
                            x = 0
                    elif diagonal_n == todas_as_diagonais_list[2]:
                        z += 1
                        y += -1
                        x += -1
                        if z > t-1:
                            z = 0
                        if y < 0:
                            y = t-1
                        if x < 0:
                            x = t-1
                    elif diagonal_n == todas_as_diagonais_list[3]:
                        z += 1
                        y += 1
                        x += -1
                        if z > t-1:
                            z = 0
                        if y > t-1:
                            y = 0
                        if x < 0:
                            x = t-1
        for diagonal_n in todas_as_diagonais_list:
            diagonal_n.sort()
            for cada_valor in diagonal_n:
                cada_valor.sort()


    i = 0

    for cada_diag in todas_as_diagonais_list:
        for cada_valor in cada_diag:
            print(cada_valor, end=' ')
            i += 1
            if i == 3:
                print('')
                i = 0
        print()




            
       
    print('Diagonais primas: ',diagonais_primas)



