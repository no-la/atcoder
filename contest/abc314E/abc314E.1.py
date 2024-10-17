N, M = map(int, input().split())
d = []
for _ in range(N):
    c, p, *s = map(int, input().split())
    s.sort()
    d.append([c, p, *s])
INF = 10**13

# 答えはmax(C[i])*M以下
e = [[INF] * (M + 1) for _ in range(N)]
# e[i][j]: ルーレットiでj以上が一回出るまでに払う金額の期待値

for i in range(N):
    j = 1
    e[i][0] = 0
    for k in range(d[i][1]):
        if k < d[i][1] - 1 and d[i][k + 2] == d[i][k + 3]:
            continue
        val = d[i][0] * d[i][1] / (d[i][1] - k)
        while j <= d[i][k + 2]:
            e[i][j] = val
            j += 1

print(*e, sep="\n")

dp = [INF] * (M + 1)
# dp[i]: iポイント獲得するために払う金額の期待値
dp[0] = 0

for i in range(1, M + 1):
    temp = min([l[i] for l in e])
    for j in range(i + 1):
        temp = min(temp, dp[j] + dp[i - j])
    dp[i] = temp

print(dp[M])
print(dp, sep="\n")
