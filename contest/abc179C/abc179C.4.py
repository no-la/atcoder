
def prime_factors_sieve(n):
    """n以下の各数の最小の素因数を求める（エラトステネスの篩）"""
    sieve = [i for i in range(n+1)]
    p = 2
    while p * p <= n:
        if sieve[p] == p:
            for q in range(p*p, n+1, p):
                if sieve[q] == q:
                    sieve[q] = p
        p += 1
    return sieve

def count_divisors(n):
    """n以下の各数の約数の個数を求める"""
    sieve = prime_factors_sieve(n)
    ans = [0] * (n+1)
    ans[1] = 1
    for i in range(2, n+1):
        current = i
        factors = 1
        while current > 1:
            p = sieve[current]
            count = 1
            while current % p == 0:
                current //= p
                count += 1
            factors *= count
        ans[i] = factors
    return sum(ans)

N = int(input())
result = count_divisors(N)
print(result)
