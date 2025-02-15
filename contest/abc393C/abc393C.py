import sys

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
d = [set([i]) for i in range(N)]
ans = 0
for _ in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    ans += u in d[v]
    d[u].add(v)
    d[v].add(u)

print(ans)
