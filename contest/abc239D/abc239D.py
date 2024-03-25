A, B, C, D = map(int, input().split())

# 高橋君が勝てるかを調べる
# あるA<=x<=Bについて、[x+C, x+D]が素数砂漠であれば勝てる

# osa_k法
MAXN = 210
sieve = [i for i in range(MAXN)] # sieve[i]: iの最も小さい素因数
p = 2
while p*p<=MAXN: # O(MAXN * loglog MAXN)
    if sieve[p]==p:
        for q in range(p*p, MAXN, p):
            if sieve[q]==q:
                sieve[q] = p
    p += 1


for x in range(A, B+1):
    for y in range(x+C, x+D+1):
        if sieve[y]==y: # yは素数
            break
    else:
        print("Takahashi")
        exit()
print("Aoki")