N, M = map(int, input().split())
A = list(map(int, input().split()))

from heapq import heapify, heappush
ranking = [[0, i+1] for i in range(N)]
heapify(ranking)
votes = [0]*N
for i in A:
    votes[i-1] += 1
    heappush(ranking, [-votes[i-1], i])
    print(ranking[0][1])