import math

def is_prime(n:int = 1):

    if n == 1 or n == 0: return False
    if n == 2: return True

    for i in range(2, n):
        if n % i == 0:
            break
    
    if i == (n-1):
        return True
    return False

def prime_list(n:int = 1) -> list:
    # n = number of primes

    primes = []
    k_prime = 1
    
    while len(primes) != n:
        if is_prime(k_prime):
            primes.append(k_prime)
        k_prime += 1
    
    return primes

def sqrt_list(p:list = []) -> list:
    q = []
    for i in range(0,len(p)):
        q.append(math.sqrt(p[i]))
    return q


if __name__ == "__main__":

    u =  sqrt_list(prime_list(1000))
    print(u)

