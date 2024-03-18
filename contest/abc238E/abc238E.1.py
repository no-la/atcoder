# https://atcoder.jp/contests/abc238/submissions/51424807
N, Q = map(int, input().split())

from collections import defaultdict, deque
d = defaultdict(list)
for _ in range(Q):
    l, r = map(lambda x: int(x)-1, input().split())
    r += 1 # [l, r)にする
    d[l].append(r)
    d[r].append(l)

# 0からたどってNに着けばYes
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