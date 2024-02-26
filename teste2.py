# definir um número n que gerara uma matriz n^n dimensões
n = 3

# definir o espaço onde as matrizes serão montadas (matriz_t 1,2 são matrizes temporárias, matriz f será o resultado da operação)
matriz_t1, matriz_t2, matriz_f = [],[],[]

for i in range(n**n-1, -1, -1):     # gera uma lista de {n,n-1,n-2,...,0}
    matriz_t1.append(i)

# Organiza as matrizes n^n por passos:

# matriz 3x3x3:
#   1º passo: organiza linhas
#   2º passo: organiza "camadas"
#   3º passo: organiza a matriz final (matriz_f)

# matriz 4x4x4x4:
#   1º passo: organiza linhas
#   2º passo: organiza "camadas"
#   3º passo: organiza células
#   4º passo: organiza a matriz final (matriz_f)

# matriz n^n, n>4:
#   1º passo: organiza linhas
#   2º passo: organiza "camadas"
#   3º passo: organiza células
#               .
#               .
#               .
#   nº passo: organiza a matriz final (matriz_f)

c = 0
while True:
    try:
        matriz_t2.append(matriz_t1[-1])
        matriz_t1.pop()

        c += 1

        if c == n:
            matriz_f.append(matriz_t2.copy())
            matriz_t2.clear()

            c = 0

    except IndexError:
        if len(matriz_f) == n:
            for i in range(0,n):
                print(f"{matriz_f[n-1-i]}\n")
            break

        matriz_t1 = matriz_f.copy()
        matriz_f.clear()


