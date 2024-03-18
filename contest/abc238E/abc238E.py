N, Q = map(int, input().split())

from collections import defaultdict, deque
d = defaultdict(list)
for _ in range(Q):
    l, r = map(lambda x: int(x)-1, input().split())
    d[l].append(r)
    d[r].append(l)

def f(start, goal, dir=1):
    #DFS
    todo = deque([start])
    seen = [False]*N #ここはsetでもよい
    seen[todo[0]] = True
    nearest = start
    while todo:
        v = todo.pop()
        if not d[v]:
            nearest += dir
            todo.append(nearest)
            seen[nearest] = True
        for w in d[v]:
            if seen[w]: #既に調べた点は飛ばす
                continue
            todo.append(w)
            seen[w] = True
            nearest = max(nearest, w)
        if nearest==goal:
            return True
    return False

print("Yes" if f(0, N-1) or f(N-1, 0, dir=-1) else "No")