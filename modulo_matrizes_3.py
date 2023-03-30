# Gerador de matriz 2x2, 3x3x3, 4x4x4x4, 5x5x5x5x5 ...

# Check list : formação da matriz, indicação das cordenas inciais
# aninda falta: criação das diagonais, verificação de primos


tamanho = 7
escopo_a = []
escopo_b = []
escopo_inicial = []

for n in range(tamanho, 0, -1):
    for p in range(tamanho**n):
        if n != tamanho:
            escopo_b.append(escopo_a[0:tamanho])
            del escopo_a[0 : tamanho]
        else:    # "gerador" de numeros
            escopo_b.append(p)
    escopo_a = escopo_b
    escopo_b = []
    if n  == tamanho-2:  # primeira !!! FACE !!!
        escopo_inicial = escopo_a[0]

print('\n\n\nFIM')