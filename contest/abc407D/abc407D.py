import sys

input = lambda: sys.stdin.readline().rstrip()
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# 全探索ですねえ
# bitで状態を持ってDFS?

N = 2 ** (H * W)


def index(i, j):
    return i * W + j


def score(grid):
    rev = 0
    for i in range(H):
        for j in range(W):
            if grid & (1 << index(i, j)):
                continue
            rev ^= A[i][j]
    return rev


# DFS
from collections import deque

ans = score(0)
todo = deque([0])
seen = [False] * N
seen[0] = True
while todo:
    v = todo.pop()
    for i in range(H):
        for j in range(W):
            k = index(i, j)
            if v & (1 << k):
                continue

            for di, dj in [(1, 0), (0, 1)]:
                ni, nj = i + di, j + dj
                if ni >= H or nj >= W:
                    continue
                l = index(ni, nj)
                if v & (1 << l):
                    continue

                w = v | (1 << k) | (1 << l)
                if seen[w]:
                    continue
                todo.append(w)
                seen[w] = True
                ans = max(ans, score(w))

print(ans)
