"""NS"""

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
MOD = 10**9 + 7
N = int(input())
C = input().split()
d = [[] for _ in range(N)]
start = None
for _ in range(N - 1):
    a, b = map(int, input().split())
    d[a - 1].append(b - 1)
    d[b - 1].append(a - 1)
    if C[a - 1] != C[b - 1]:
        start = a - 1


# a-b の辺を1点とみなして、その間の辺を1回以下ずつ切る場合の数を出す
# DFSもどき
edges = []
todo = [(start, 0)]
seen = [False] * N
seen[start] = True
while todo:
    v, c = todo.pop()
    nc = c + 1
    for w in d[v]:
        if seen[w]:
            continue
        if C[v] != C[w]:
            edges.append(c)
            todo.append((w, 0))
        else:
            todo.append((w, nc))
        seen[w] = True


ans = 1
