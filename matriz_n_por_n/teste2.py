import json

# definir um número n que gerara uma matriz n^n dimensões
n = 3

# definir o espaço onde as matrizes serão montadas (matriz_t 1,2 são matrizes temporárias, matriz f será o resultado da operação)
matriz_t1, matriz_t2, matriz_f = [],[],[]

# for i in range(n**n-1, -1, -1):     # gera uma lista de {n,n-1,n-2,...,0}
#     matriz_t1.append(i)

for i in range(0, n**n):
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
            # with open("matriz_n_por_n\matriz_f.json", "w") as input:
            #     json.dump(matriz_t2, input)
            # with open("matriz_n_por_n\matriz_f.json", "r") as openfile:
            #     matriz_f = json.load(openfile)
            matriz_t2.sort()
            matriz_f.append(matriz_t2.copy())
            matriz_t2.clear()
            c = 0

    except IndexError:
        if len(matriz_f) == n:
            # matriz_f.sort()
            # for i in range(0,n):
            #     print(f"{matriz_f[n-1-i]}\n")
            break
        else: pass

        matriz_t1 = matriz_f.copy()
        matriz_f.clear()


with open("matriz_n_por_n\matriz_f.json", "w") as arquivo:
    json.dump(matriz_f, arquivo)

with open("matriz_n_por_n\matriz_f.json", "r") as arquivo:
    print(json.load(arquivo))


print("FIM")