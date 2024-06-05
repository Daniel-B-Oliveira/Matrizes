def g_list() -> list:
    ...


def agroup(le:int = 1, n:int = 1, base:list = [], autocomplet: bool = False) -> list:
    '''
        le: number of elements in each list
        n: number of list with le elements
        base: list that will be grouped
        autocomplet: complete the matrix with None value
    '''

    out_matrix = []
    
    if autocomplet == True and len(base) < (le*n):
        for i in range(0, len(base)-le*n):
            base.append(None)

    if n == 0:
        return out_matrix
    
    for k in range(0, n):
        out_matrix.append(base[k*le:(k+1)*le])

    return out_matrix

def mult_agroup(dimensions:int = 1, groups:list = []) -> list:
    '''
        dimensions: number of times func:agroup will be done
        groups: input list
    '''
    n = dimensions
    matrix = groups
    for k in range(0, n-1):
        matrix = agroup(n, n**(n-k-1), matrix)
    return matrix

def is_prime(number:int = 1) -> bool:
    if number < 2:
        return False
    for k in range(2, number):
        if number % k == 0:
            return False
    return True

def determinant(matrix:list = []) -> list:
    len_matrix = len(matrix)
    for i in range(0, len_matrix**2):
        if i != 0: break
        seconde=[]
        for j in range(0, len_matrix):
            initial_matrix = matrix[j]
            for k in range(0, len_matrix-1):
                initial_matrix = initial_matrix[j]
                print(j,k,initial_matrix)
            seconde.append(initial_matrix)

    print(seconde)
    return ...

if __name__ == "__main__":
    import json

    n = int(input("Digite um valor: "))
    qst = 0
    while qst not in (1,2):
        qst = int(input("Valor do numero(1), valor da funcao e primo(2): "))

    numbers = []

    if qst == 2:
        for i in range(1, n**n+1):
            numbers.append(is_prime(i))
    else:
        for i in range(1, n**n+1):
            numbers.append(i)


    # for k in range(0, n-1):
    #     numbers = agroup(n, n**(n-k-1), numbers)

    with open("matriz_n_por_n\matriz.json", "w") as file:
        json.dump(mult_agroup(n,numbers), file)

    print(mult_agroup(n, numbers))
    print(determinant(mult_agroup(n, numbers)))

