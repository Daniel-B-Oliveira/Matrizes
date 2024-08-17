import math

def is_prime(n:int):
    if n < 2: return False

    for i in range(2,n):
        if i*i > n: break
        if(n%i == 0): return False
    
    return True 
    

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

    p =  prime_list(100)
    print(p)

    #make a point (x,y), where x = sqrt_p and y = p 

    points = []

    for i in range(0,len(p)):
        point = (math.sqrt(p[i]), p[i])
        points.append(point)
        print(point)