from collections import deque

N, M = map(int, input().split())
H = list(map(int, input().split()))
d = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    d[u].append(v)
    d[v].append(u)


# 決め打ちにぶたん
l, r = 0, 10**15
while l < r - 1:  # lはあり得る、rはあり得ない
    c = (l + r) // 2
    # DFS
    todo = deque([(0, 0)])  # 頂点, 楽しさ
    seen = set([0])
    over = False
    while todo and not over:
        v, vjoy = todo.pop()
        for w in d[v]:
            if w in seen:
                continue
            delta = H[v] - H[w] if H[v] >= H[w] else 2 * (H[v] - H[w])
            wjoy = vjoy + delta
            over = over or wjoy >= c
            todo.append((w, wjoy))
            seen.add(w)
    if over:
        l = c
    else:
        r = c

print(l)
