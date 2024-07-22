H, W, Y = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

from heapq import heapify, heappop, heappush
#heapify(a:list)
#heappop(a) (最小値)
#heappush(a, value)
hq = [] # 海面に面している区画のキュー
seen = [[False]*W for _ in range(H)]
heapify(hq)
for i in range(H):
    heappush(hq, (A[i][0], i, 0))
    seen[i][0] = True
    if not seen[i][W-1]:
        heappush(hq, (A[i][W-1], i, W-1))
        seen[i][W-1] = True
for j in range(1, W-1):
    heappush(hq, (A[0][j], 0, j))
    seen[0][j] = True
    if not seen[H-1][j]:
        heappush(hq, (A[H-1][j], H-1, j))
        seen[H-1][j] = True

ans = H*W
for y in range(1, Y+1):
    while hq and hq[0][0]<=y:
        _, i, j = heappop(hq)
        # print(y, i, j)
        ans -= 1
        for di, dj in [[0, -1],[0, 1],[-1, 0],[1, 0]]:
            ni, nj = i+di, j+dj
            if not (0<=ni<H and 0<=nj<W):
                continue
            if seen[ni][nj]:
                continue
            seen[ni][nj] = True
            heappush(hq, (A[ni][nj], ni, nj))

    print(ans)

