from heapq import heapify, heappop, heappush

N, K = map(int, input().split())
A = list(map(int, input().split()))

# その時選べる最大を選ぶだけじゃないの？
i = 0
scores = [0, 0]
remain = N
hq = [-a for a in A]
heapify(hq)
while hq:
    while hq and -hq[0] > remain:
        heappop(hq)

    if hq:
        tar = -hq[0]
        scores[i] += tar
        remain -= tar
        i ^= 1
    # print(i, scores, tar, remain)

print(scores[0])
