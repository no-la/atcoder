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

K = 11

can_zero = [False] * K

for k in range(K - 1, -1, -1):
    # DFS
    todo = deque([(0, 0)])
    seen = [[False] * 2 for _ in range(N)]
    seen[0][0] = True
    while todo:
        (v, v_bit) = todo.pop()
        for w, c in E[v]:
            w_bit = (v_bit ^ c) & (1 << k) != 0
            if seen[w][w_bit]:
                continue
            todo.append((w, w_bit))
            seen[w][w_bit] = True

    can_zero[k] = seen[N - 1][0]
    print(k, seen)

print(sum([(not b) * (2**k) for k, b in enumerate(can_zero)]))
