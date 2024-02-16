X, Y, A, B, C = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))

P.sort(reverse=True)
Q.sort(reverse=True)
R.sort(reverse=True)
PQR = [P, Q, R]
ABC = [A, B, C]
XY = [X, Y]

dp = [[0, 0, 0, 0] for _ in range(X+Y+1)] # dp[i]: 合計i個食べるときの最大値, 赤の個数, 緑の個数, 無色の個数
for i in range(1, X+Y+1):
    cur_max = 0
    pre_max, *ids = dp[i-1]
    max_i = -1
    for j in range(3):
        if j < 2 and ids[j]>=XY[j]:
            continue
        if ids[j]>=ABC[j]:
            continue
        m = PQR[j][ids[j]]
        if cur_max<m:
            cur_max = m
            max_i = j
    ids[max_i] += 1
    dp[i][0] = pre_max + cur_max
    for k in range(3):
        dp[i][1+k] = ids[k]
    # print(i, dp)
print(dp[-1][0])