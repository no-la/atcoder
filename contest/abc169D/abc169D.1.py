import math
N = int(input())
A = 10**6 + 100

# 1のときだけ0になる
if N==1:
    print(0)
    exit()


# O(sqrt(N))で素因数分解
d = [0]*A
for n in range(2, A):
    while N%n==0:
        d[n] += 1
        N = N//n


ans = 0

for r in d: # rは各因数の指数
    i = 0
    while r>=i+1:
        i += 1
        r -= i
    ans += i
ans += N>1 # Nの素因数にAより大きい素数があるとき、N>1となる。このとき、ans++する。
print(ans if ans!=0 else 1)