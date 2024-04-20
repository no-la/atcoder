import math
N, M = map(int, input().split())
from collections import defaultdict
d = defaultdict(list)
for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    d[a].append(b)
    d[b].append(a)


from collections import deque
ans = 0
seen = [False]*N # ここはsetでもよい
for s in range(N):
    if seen[s]:
        continue
    # DFS
    count = 1
    edge_num = 0
    todo = deque([s])
    seen[todo[0]] = True
    while todo:
        v = todo.pop()
        for w in d[v]:
            edge_num += 1
            if seen[w]: # 既に調べた点は飛ばす
                continue
            todo.append(w)
            seen[w] = True
            count += 1
    # print(s, count, edge_num//2)
    ans += math.comb(count, 2)-edge_num//2

print(ans)
