N, M = map(int, input().split())
d = [[] for _ in range(N)]
for i in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    d[u].append((v, i))
    d[v].append((u, i))

# 連結成分ごとに考える
# - 連結成分間の任意の頂点の組み合わせは可能である
# - 連結成分内では、各頂点に0, 1を振っていって、(0の個数)x(1の個数)-辺の本数が答えになる
# これらの和を足し合わせたものが答えになる

ans = 0

group_sizes = []  # 工夫が必要な気がするので後で考える


# 連結成分を調べるのと、
# 連結成分ごとの答えを出す
from collections import deque

value = [None] * N
for i in range(N):
    if value[i] is not None:
        continue
    value[i] = 0

    count = [1, 0]
    edges = set()
    # DFS
    todo = deque([i])
    while todo:
        v = todo.pop()
        w_value = value[v] ^ 1
        for w, e in d[v]:
            edges.add(e)
            if value[w] is not None:
                if w_value != value[w]:  # 二部グラフでない
                    print(0)  # 全体も二部グラフでない
                    exit()
                continue
            todo.append(w)
            count[w_value] += 1
            value[w] = w_value
    group_sizes.append(sum(count))
    ans += count[0] * count[1] - len(edges)


# 連結成分間の組み合わせ
group_sum = sum(group_sizes)
tmp = 0
for s in group_sizes:
    tmp += s * (group_sum - s)

ans += tmp // 2

print(ans)
