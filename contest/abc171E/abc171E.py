N = int(input())
A = list(map(int, input().split()))


d = [0]*(N+1) # d[i]: [0, i)のxor
# 累積xor
for i in range(1, N+1):
    d[i] = d[i-1] ^ A[i-1]


print(*[d[i] ^ (d[-1]^d[i+1]) for i in range(N)])
