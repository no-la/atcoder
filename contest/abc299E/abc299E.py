from collections import deque

N, M = map(int, input().split())
INF = -1
E = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    E[u].append(v)
    E[v].append(u)

dist = [[INF] * N for _ in range(N)]
for i in range(N):
    # BFS
    todo = deque([i])
    dist[i][i] = 0
    while todo:
        v = todo.popleft()
        for w in E[v]:
            if dist[i][w] != -1:  # 既に調べた点は飛ばす
                continue
            todo.append(w)
            dist[i][w] = dist[i][v] + 1


# 各pに対してあり得る頂点を洗い出す
K = int(input())
if K == 0:
    print("Yes")
    print("1" + "0" * (N - 1))
    exit()

need = []
cannot = set()
for i in range(K):
    p, d = map(int, input().split())
    p -= 1
    need.append([])
    for j in range(N):
        if dist[p][j] == d:
            need[i].append(j)
        elif dist[p][j] < d:
            cannot.add(j)

# print(*dist, sep="\n")
# print(need, cannot, sep="\n")

ans = set()
for i in range(K):
    for j in need[i]:
        if j not in cannot:
            ans.add(j)
            break
    else:
        print("No")
        exit()

ans = [1 if i in ans else 0 for i in range(N)]
print("Yes")
print(*ans, sep="")
