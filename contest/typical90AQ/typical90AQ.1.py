import sys

input = lambda: sys.stdin.readline().rstrip()
import heapq


def dijkstra(edges, N, start=0):
    """
    parameter
        edges[i][_] : [点iから向かう点, コスト]
        N : 点の個数(=len(edges))
        start : 探索を始める点
    """
    dist = [float("inf")] * N  # dist[i]: startからiまでのコスト
    dist[start] = 0  # スタートは0
    seen = [False] * N

    hq = []  # コスト, 向かう点, direction
    heapq.heappush(hq, (0, start, None))

    while hq:
        _, current, direction = heapq.heappop(hq)

        if seen[current]:  # 同じ点を二度見ない
            continue
        seen[current] = True
        for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            i, j = divmod(current, W)
            i += di
            j += dj
            if not (0 <= i < H and 0 <= j < W):
                continue
            if S[i][j] == "#":
                continue
            to = i * W + j
            to_direction = to - current
            cost = direction is not None and direction != to_direction
            # print(divmod(current, W), "->", divmod(to, W), ":", cost)
            if (
                dist[current] + cost < dist[to]
            ):  # 最短距離を更新できるときだけheappush()
                dist[to] = dist[current] + cost
                heapq.heappush(hq, (dist[current] + cost, to, to_direction))
    return dist


H, W = map(int, input().split())
s = tuple(map(lambda x: int(x) - 1, input().split()))
t = tuple(map(lambda x: int(x) - 1, input().split()))
S = [input() for _ in range(H)]

dist = dijkstra([], H * W, s[0] * W + s[1])
# print(*[dist[W * i : W * (i + 1)] for i in range(H)], sep="\n")
print(dist[t[0] * W + t[1]])
