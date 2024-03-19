import math
N = int(input())
M = int(N**0.5)+1

ans = 0
# O(sqrt(N))で素因数分解
for n in range(2, M):
    i = 1
    while N%(n**i)==0:
        ans += 1
        N //= n**i
        i += 1
    # わだかまりをなくすために、割れるだけ割っておく
    while N%n==0:
        N //= n

ans += N>1 # 残ったNが素数のときは、z=Nの分の1を足す
print(ans)