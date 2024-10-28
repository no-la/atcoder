import math

T = int(input())
for _ in range(T):
    N, D, K = map(int, input().split())
    K -= 1
    e = N // math.gcd(N, D)
    # e回でx=0に帰ってくる
    ans = K // e + D * (K % e)
    ans %= N
    print(ans)
