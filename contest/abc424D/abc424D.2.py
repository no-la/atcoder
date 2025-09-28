T = int(input())

INF = 10**9


X = 2**7
is_ok = [[False] * X for _ in range(X)]
for i in range(X):
    for j in range(X):
        for t in range(6):
            l, r = 1 << t, 1 << (t + 1)
            lu, ru = i & l, i & r
            ld, rd = j & l, j & r
            if lu and ru and ld and rd:
                break
        else:
            is_ok[i][j] = True


def solve(H, W, S):
    K = 2**W
    dp = [[INF] * K for _ in range(H + 1)]
    dp[0][0] = 0
    # dp[i][j]: i-1行目までOKで, i行目がjの状態であるときの最小操作回数
    # j は bit で、1なら黒

    # 全体で 2^7 * 7 * 2^7 * 7 = 802816 ~ 10^6
    for i in range(H):  # 7
        ni = i + 1
        for j in range(K):  # 2^7 = 128
            for nj in range(K):  # 2^7 = 128
                if not is_ok[j][nj]:
                    continue

                dp[ni][nj] = min(
                    dp[ni][nj],
                    dp[i][j]
                    + sum(
                        [(nj & (1 << x)) == 0 and S[ni - 1][x] == "#" for x in range(W)]
                    ),
                )
    print(min(dp[H]))
    # print(*dp, sep="\n")


for _ in range(T):
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    solve(H, W, S)
