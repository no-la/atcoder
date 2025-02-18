import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
cant = [set() for _ in range(N)]
for _ in range(M):
    x, y = map(lambda x: int(x) - 1, input().split())
    cant[x].add(y)
    cant[y].add(x)

INF = 10**10

ans = INF
# 10!~3.6*10^6
# 順列 O(nPk)<=n!
import itertools

for l in itertools.permutations(range(N), N):
    time = 0
    for j, i in enumerate(l):
        time += A[i][j]
        if j + 1 < N and l[j + 1] in cant[i]:
            break
    else:
        ans = min(ans, time)

if ans == INF:
    ans = -1

print(ans)
