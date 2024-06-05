tamanho_matriz = 3

num = (n for n in range(tamanho_matriz**3))

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

todas_as_diagonais_list = [[],[],[],[]]

diagonais_iniciais = [
        (lin,col,cam)
        for cam in range(tamanho_matriz)
        for lin in range(tamanho_matriz)
        for col in range(tamanho_matriz)
        if cam == 0
    ]

def diagonal_1(z,y,x):
    z += 1
    y += 1
    x += 1
    if z > tamanho_matriz-1:
        z = 0
    if y > tamanho_matriz-1:
        y = 0
    if x > tamanho_matriz-1:
        x = 0
    return z, y, x



def diagonal_2(z,y,x):
    z += 1
    y += -1
    x += 1
    if z > tamanho_matriz-1:
        z = 0
    if y < 0:
        y = tamanho_matriz-1
    if x > tamanho_matriz-1:
        x = 0
    return z, y, x


def diagonal_3(z,y,x):
    z += 1
    y += -1
    x += -1
    if z > tamanho_matriz-1:
        z = 0
    if y < 0:
        y = tamanho_matriz-1
    if x < 0:
        x = tamanho_matriz-1
    return z, y, x


def diagonal_4(z,y,x):
    z += 1
    y += 1
    x += -1
    if z > tamanho_matriz-1:
        z = 0
    if y > tamanho_matriz-1:
        y = 0
    if x < 0:
        x = tamanho_matriz-1
    return (z, y, x)


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
                    l = diagonal_1(z=z, y=y, x=x)
                    z = l[0]
                    y = l[1]
                    x = l[2]
                elif diagonal_n == todas_as_diagonais_list[1]:
                    l = diagonal_2(z=z, y=y, x=x)
                    z = l[0]
                    y = l[1]
                    x = l[2]
                elif diagonal_n == todas_as_diagonais_list[2]:
                    l = diagonal_3(z=z, y=y, x=x)
                    z = l[0]
                    y = l[1]
                    x = l[2]
                elif diagonal_n == todas_as_diagonais_list[3]:
                    l = diagonal_4(z=z, y=y, x=x)
                    z = l[0]
                    y = l[1]
                    x = l[2]

print('FIM')

print(todas_as_diagonais_list)