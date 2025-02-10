import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())

E = [[] for _ in range(N)]
reversed_E = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    E[a].append(b)
    reversed_E[b].append(a)

# 1回目のDFS（順方向グラフ）: 反復的DFSで終了時刻順を求める
visited = [False] * N
finish_order = []

for i in range(N):
    if not visited[i]:
        stack = deque()
        stack.append((i, False))  # (現在の頂点, 処理完了フラグ)
        while stack:
            v, finished = stack.pop()
            if finished:
                finish_order.append(v)
                continue
            if visited[v]:
                continue
            visited[v] = True
            stack.append((v, True))  # 処理完了後に戻るために再度追加
            for next_v in E[v]:
                if not visited[next_v]:
                    stack.append((next_v, False))

# 2回目のDFS（逆方向グラフ）: 反復的DFSで強連結成分を探索
visited = [False] * N
ans = 0

for v in reversed(finish_order):
    if not visited[v]:
        stack = deque([v])
        component_size = 0
        while stack:
            node = stack.pop()
            if visited[node]:
                continue
            visited[node] = True
            component_size += 1
            for next_node in reversed_E[node]:
                if not visited[next_node]:
                    stack.append(next_node)
        if component_size > 1:
            ans += component_size * (component_size - 1) // 2  # 強連結成分内のペア数

print(ans)
