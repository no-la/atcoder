from collections import deque

N = int(input())
E = [tuple(map(int, input().split())) for _ in range(N)]
INF = 10**10

# 決め打ちにぶたん
l, r = 0, INF
while l < r - 1:
    c = (l + r) // 2

    # init
    d = [[] for _ in range(N)]
    for i in range(N):
        sx, sy, sp = E[i]
        for j in range(N):
            gx, gy, gp = E[j]
            if sp * c >= abs(sx - gx) + abs(sy - gy):
                d[i].append(j)
    # print(*d, sep="\n")
    # DFS
    for i in range(N):
        todo = deque([i])
        seen = set([i])
        while todo:
            v = todo.pop()
            for w in d[v]:
                if w in seen:
                    continue
                todo.append(w)
                seen.add(w)
        if len(seen) == N:
            r = c
            break
    else:
        l = c

print(r)
