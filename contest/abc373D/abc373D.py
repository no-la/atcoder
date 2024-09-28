from collections import deque

N, M = map(int, input().split())
d = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    d[u].append((v, w))
    d[v].append((u, -w))
K = 10**18

ans = [None] * N

for i in range(N):
    if ans[i] is not None:
        continue
    temp = dict()
    l, r = -K, K
    while True:
        c = (l + r) // 2
        # DFS
        todo = deque([i])
        temp[i] = c
        seen = set()
        seen.add(i)
        ok = True
        while todo:
            v = todo.pop()
            for w, wc in d[v]:
                if w in seen:  # 既に調べた点は飛ばす
                    continue
                if temp[v] + wc < -K:
                    ok = False
                    l = c
                    break
                if K < temp[v] + wc:
                    ok = False
                    r = c
                    break
                todo.append(w)
                seen.add(w)
                temp[w] = temp[v] + wc
        if ok:
            break

    for k, v in temp.items():
        ans[k] = v

print(*ans, sep=" ")
