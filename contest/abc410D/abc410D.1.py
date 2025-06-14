import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

# 拡張DFSみたいな
N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    E[a].append((b, w))

K = 2**10

# DFS
todo = deque([(0, 0)])
seen = [[False] * K for _ in range(N)]
seen[0][0] = True
while todo:
    (v, v_bit) = todo.pop()
    for w, c in E[v]:
        w_bit = v_bit ^ c
        if seen[w][w_bit]:
            continue
        todo.append((w, w_bit))
        seen[w][w_bit] = True


tar = [i for i in range(K) if seen[N - 1][i]]

if not tar:
    print(-1)
else:
    print(min(tar))
