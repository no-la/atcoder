N, Q = map(int, input().split())

from collections import defaultdict, deque
d = defaultdict(list)
for _ in range(Q):
    l, r = map(lambda x: int(x)-1, input().split())
    r += 1
    d[l].append(r)
    d[r].append(l)

#DFS
todo = deque([0])
seen = [False]*N #ここはsetでもよい
seen[todo[0]] = True
nearest = 0
while todo:
    v = todo.pop()
    for w in d[v]:
        if w==N:
            print("Yes")
            exit()
        if seen[w]: #既に調べた点は飛ばす
            continue
        todo.append(w)
        seen[w] = True
print("No")