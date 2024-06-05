"""
    Digitar um valor x e encontrar qual valor C(n,k) = x 
"""

def fatorial(n_value:int = 0):  
    if n_value == 0: return 1
    elif n_value < 0: raise ValueError("fatorial function: n < 0")

    f = 1
    for k in range(n_value , 0, -1):
        f = f*k
    return int(f)

def combinatoria(n_value:int = 0, k_value: int = 0):

    if n_value == 0: return 1
    elif n_value < 0: raise ValueError("fatorial function: n < 0")
    elif n_value < k_value: ValueError("combinatoria function: n < k")

    f = 1
    for k in range(n_value , n_value - k_value, -1):
        f = f*k

    return int(f / fatorial(k_value))

# def combinatoria(n:int =0, k:int =0):
#     if n < k: raise ValueError("combinatoria function: n < k")

#     return int(fatorial(n)/(fatorial(n-k)*fatorial(k)))


def e_combinatoria(x:int =0):
    if x <= 0: raise ValueError("e_combinatoria function: x <= 0")

    for linha_n0 in range(0,x+1):    # número de linhas

        """
            Realiza apenas metada das operações, pois são simétricas
                C(N , K) = C(N , N-k)
            Para k par:
                é preciso realizar a metade das operações
            Para k impar:
                é preciso realizar a metade das operações + 0.5
                ex: metade de 3 = 1.5
                    deve-se realizar: 1.5 + 0.5 = 2 operações
                 
        """
        index = int(linha_n0/2+1) if linha_n0 % 2 == 0 else int(linha_n0/2+1.5)
        x_menor_combi = 0
        # print(f"{linha_n0}")
        for i in range(0,index):    # colunas
            valor_analisado = combinatoria(linha_n0, i)
            if valor_analisado == int(x): return (linha_n0,i,-1)
            if x < valor_analisado:
                x_menor_combi += 1
            if x_menor_combi == index - 2 and index != 2:
                # retorna a linha em que ja se torna impossível ter o valor x
                # com exceção de quando x = C(x,1) ou c(x,x-1)
                return(x,1,int(linha_n0))

if __name__ == "__main__":
    while True:
        x = (input("Digite um número inteiro: "))
        try:
            x = int(x)
            comb = e_combinatoria(x)
            print(f"C({comb[0]},{comb[1]}) = {x} ou "
                  f"C({comb[0]},{comb[0]-comb[1]}) = {x}")
            print(f"linha de incerteza {comb[2]}")
        except ValueError:
            print(f"{x} é um valor inválido")
            pass
        except OverflowError:
            print(f"{x} é um valor muito grande para essa operação")



# for n in range(0,25):
#     print(f"l{n}", end=": ")
#     for k in range (0, n+1):
#         print(combinatoria(n,k), end= " ")
#     print()