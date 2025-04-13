import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
A = list(map(int, input().split()))

# imos法
imos = [0] * N  # 増分
ans = [0] * N
for i in range(N):
    use = min(N - i - 1, A[i])
    ans[i] = A[i] - use
    if i + 1 < N:
        imos[i + 1] += 1
    if i + use + 1 < N:
        imos[i + use + 1] -= 1

for i in range(1, len(imos)):
    imos[i] += imos[i - 1]

for i in range(N):
    ans[i] += imos[i]

print(*ans)
