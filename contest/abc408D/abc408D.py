import sys

input = lambda: sys.stdin.readline().rstrip()
T = int(input())
INF = 10**9


def solve(N, S):
    dp = [[INF] * 3 for _ in range(N + 1)]
    # dp[i][t]: i 文字までOKで、まだ1は出ていない(t=0) or 直前に1が出た(t=1) or 既に1がで終えた(t=2)ときの最小値

    dp[0][0] = 0
    for i in range(N):
        # 1 が出ないまま
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + (S[i] != "0"))
        # はじめて 1 が出る
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][0] + (S[i] != "1"))
        # 1 が続く
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][1] + (S[i] != "1"))
        # 1 が続かない
        dp[i + 1][2] = min(dp[i + 1][2], dp[i][1] + (S[i] != "0"))
        # 1 がで終えていて 0 が続く
        dp[i + 1][2] = min(dp[i + 1][2], dp[i][2] + (S[i] != "0"))

    print(min(dp[N]))


for _ in range(T):
    N = int(input())
    S = input()
    solve(N, S)
