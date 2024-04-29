N, K = map(int, input().split())

def f(x):
    # y+z = x なる 1<=y,z<=N の個数
    # y = x-z, 1<=x-z<=N
    # x-N<=z<=x-1
    # print(x, min(x-1, N), max(x-N-1, 0))
    v = min(x-1, N)-max(x-N-1, 0)
    return max(0, v)

# 2<=c+d<=2*N
# a+b = K+ c+d, K+2<=a+b<=K+2*N
ans = 0
for ab in range(K+2, K+2*N+1):
    # print("-"*10)
    # print(ab, "-", ab-K, "=", K)
    ans += f(ab)*f(ab-K)

print(ans)
