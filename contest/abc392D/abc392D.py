import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
A = [list(map(int, input().split()))[1:] for _ in range(N)]
M = 10**5

d = [[0] * (M + 1) for _ in range(N)]
# d[i][j]: サイコロiでjを出す確率

for i in range(N):
    for a in A[i]:
        d[i][a] += 1 / len(A[i])

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        temp = 0
        for a in range(1, M + 1):
            temp += d[i][a] * d[j][a]
        ans = max(ans, temp)

print(ans)
