from heapq import heapify, heappop, heappush

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = sorted([(a, b) for a, b in zip(A, B)])
    # print(A, B, sep="\n")

    Q = []
    heapify(Q)
    bsum = 0
    ans = 10**18
    for i in range(N):
        a, b = C[i]
        heappush(Q, -b)
        bsum += b
        if len(Q) == K:
            ans = min(ans, a * bsum)
            bsum -= -heappop(Q)
    print(ans)
