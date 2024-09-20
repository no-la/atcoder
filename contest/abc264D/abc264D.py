from collections import defaultdict, deque

S = input()

# BFS
todo = deque(["atcoder"])
dist = defaultdict(lambda: -1)
dist[todo[0]] = 0
while todo:
    v = todo.popleft()
    for i in range(6):
        w = v[:i] + v[i + 1] + v[i] + v[i + 2 :]
        if dist[w] != -1:  # 既に調べた点は飛ばす
            continue
        todo.append(w)
        dist[w] = dist[v] + 1

print(dist[S])
