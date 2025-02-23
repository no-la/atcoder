import sys

input = lambda: sys.stdin.readline().rstrip()
H, W = map(int, input().split())
s = tuple(map(lambda x: int(x) - 1, input().split()))
t = tuple(map(lambda x: int(x) - 1, input().split()))
S = [input() for _ in range(H)]

from heapq import heapify, heappop, heappush

lrud = [[0, -1], [0, 1], [-1, 0], [1, 0]]
hq = [(0, s[0], s[1], None)]
heapify(hq)
seen = [[False] * W for _ in range(H)]
seen[s[0]][s[1]] = True

while hq:
    c, vi, vj, direction = heappop(hq)
    print(vi, vj)
    if (vi, vj) == t:
        print(c)
        exit()
    for di, dj in lrud:
        ni, nj = vi + di, vj + dj
        if not (0 <= ni < H and 0 <= nj < W):
            continue
        if S[ni][nj] == "#":
            continue
        if seen[ni][nj]:
            continue
        seen[ni][nj] = True
        nc = c + (direction is not None and (di, dj) != direction)
        heappush(hq, (nc, ni, nj, (di, dj)))
