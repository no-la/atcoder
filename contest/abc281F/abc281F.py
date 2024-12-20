N = int(input())
A = list(map(int, input().split()))

# 都度、一番大きいものを、他にそれより大きいものが出ないように、小さくしていく

from heapq import heapify, heappop, heappush

hq = []
for a in A:
    heappush(hq, -a)

x = [None] * 30
