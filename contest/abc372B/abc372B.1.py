from collections import deque

M = int(input())
X = 10
N = 20
# DFS
todo = deque([[[], 0]])
while todo:
    vl, vs = todo.pop()
    for w in range(X + 1):
        ws = vs + 3**w
        wl = vl + [w]
        if ws > M:
            continue
        elif ws == M:
            print(len(wl))
            print(*wl)
            exit()

        if len(wl) < N:
            todo.append([wl, ws])
