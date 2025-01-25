N, X = map(int, input().split())
d = [[], [], []]
for _ in range(N):
    v, a, c = map(int, input().split())
    d[v - 1].append((a, c))


# 前計算
dp = [[[0] * (X + 1) for _ in range(len(d[v]) + 1)] for v in range(3)]
# dp[v][i][j]: d[v][:i]まで見てカロリーj以下ときの最大摂取量

for v in range(3):
    for i in range(len(d[v])):
        a, c = d[v][i]
        for j in range(X + 1):
            dp[v][i + 1][j] = max(dp[v][i + 1][j], dp[v][i][j])
            if j + c <= X:  # 食べるとき
                dp[v][i + 1][j + c] = max(dp[v][i + 1][j + c], dp[v][i][j] + a)


ans = 0
for c0 in range(X + 1):
    for c1 in range(X + 1 - c0):
        c2 = X - c0 - c1
        ans = max(
            ans, min(dp[0][len(d[0])][c0], dp[1][len(d[1])][c1], dp[2][len(d[2])][c2])
        )

print(ans)
