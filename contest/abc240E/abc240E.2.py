N = int(input())
from collections import defaultdict
d = defaultdict(list)
for _ in range(N-1):
    u, v = map(lambda x: int(x)-1, input().split())
    d[u].append(v)
    d[v].append(u)

parent = [-1] * N
leaf_num = [0] * N

# DFSで各ノードの親と葉の数を計算する
stack = [0]
while stack:
    node = stack.pop()
    if node != 0 and len(d[node]) == 1:  # 葉ノードの場合
        leaf_num[node] = 1
    for neighbor in d[node]:
        if parent[node] == neighbor:  # 親への逆戻りを防ぐ
            continue
        parent[neighbor] = node
        stack.append(neighbor)
        leaf_num[node] += leaf_num[neighbor]

# 各ノードの左端と右端を計算する
left = [0] * N
right = [0] * N
current = 0
for node in range(N):
    if parent[node] == -1 or node == 0 or len(d[node]) > 1:
        left[node] = current
        right[node] = current + leaf_num[node] - 1
        current = right[node] + 1

# 結果を出力する
for node in range(N):
    print(left[node] + 1, right[node] + 1)
