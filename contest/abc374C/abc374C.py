N = int(input())
K = list(map(int, input().split()))

ans = 10**15
# bit全探索
for i in range(2**N):
    a = 0
    b = 0
    for j in range(N):
        if not ((i >> j) & 1):
            a += K[j]
        else:
            b += K[j]
    ans = min(ans, max(a, b))

print(ans)
