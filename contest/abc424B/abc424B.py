import sys

input = lambda: sys.stdin.readline().rstrip()
N, M, K = map(int, input().split())
ans = []
d = [0] * N
for _ in range(K):
    a, b = map(int, input().split())
    a -= 1
    d[a] += 1
    if d[a] == M:
        ans.append(a + 1)

print(*ans)
