H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
N = int(input())
for i in range(N):
    r, c, e = map(int, input().split())
    A[r-1][c-1] = e
HH, WW = H+1, W+1
HHWW = HH*WW+100
dp = [[[0, set()] for __ in range(WW)] for _ in range(HH)]
# dp[i][j]: [(i, j)に辿り着いたときのエネルギーの最小値, 既に使った薬の座標]





