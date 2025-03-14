import sys

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
d = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    d[a].append(b)
    d[b].append(a)


def f(i, l):
    return 1 == sum([a < i for a in l])


print(sum([f(i, l) for i, l in enumerate(d)]))
