# Gerador de matriz 2x2, 3x3x3, 4x4x4x4, 5x5x5x5x5 ...

# Check list : formação da matriz, indicação das cordenas inciais
# aninda falta: criação das diagonais, verificação de primos


tamanho = 3

escopo_a = []
escopo_b = []
escopo_principal = []

for n in range(tamanho, 0, -1):
    for p in range(tamanho**n):
        if n != tamanho:
            escopo_b.append(escopo_a[0:tamanho])
            del escopo_a[0 : tamanho]
        else:    # "gerador" de numeros
            escopo_b.append(p+1)
    escopo_a = escopo_b
    escopo_b = []
    if n  == tamanho-2:  # primeira !!! FACE !!!
        escopo_principal = escopo_a[0]

escopo_principal = escopo_a

print(escopo_principal)

cordenadas_primeira = []

for n in range (0, tamanho):
    cordenada = []
    for j in range(0, tamanho):
        num = 0
        num += n
        cordenada.append(num)
    cordenadas_primeira.append(cordenada)

# print(cordenadas_primeira)

escopa_camada = []

# for n in range(0, tamanho):

n = 0
for i in range(tamanho):
    print(escopo_principal[n][n][n])
    n += 1

treco_outro = (tamanho**tamanho+1)/2

print(treco_outro)