import math
T = int(input())
for i in range(T):
    N = int(input())
    primes = []
    m = N
    for j in range(int(math.sqrt(N))):
        while(m % j == 0):
            primes.append(j)
            m //= j