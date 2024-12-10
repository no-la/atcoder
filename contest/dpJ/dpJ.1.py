N = int(input())
A = list(map(int, input().split()))
sa = sum(A)

dp = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(sa + 1)]
# dp[s][i][j]: 寿司が全部でs個残っていて、1つの皿がi個、2つの皿がj個にするための操作回数の期待値

c1 = A.count(1)
c2 = A.count(2)

dp[sa][c1][c2] = 0

for s in range(sa - 1, -1, -1):
    for si in range(min(N * 1, s), -1, -1):
        i = si
        for sj in range(min(N * 2, s - si), -1, -1):
            if sj % 2 != 0:
                continue
            j = sj // 2
            sk = s - si - sj
            if sk < 0 or sk % 3 != 0:
                continue
            k = sk // 3
            print(s, i, j, k)
            if i + j + k == N:
                continue
            if i + j + k + 1 == N:
                dp[s][i][j] = 1
                continue
            # p = sum([(l+1)*((N-(i+j+k+1))/N)^l] for l in range(INF))
            p = N**2 / ((i + j + k + 1) ** 2)

            if i + 1 <= N:
                x = dp[s + 1][i + 1][j]
                dp[s][i][j] += ((x + 1) * N / (i + j + k + 1) + p) * (i + 1) / N
            if i - 1 >= 0 and j + 1 <= N:
                q = N**2 / ((i + j + k) ** 2)
                x = dp[s + 1][i - 1][j + 1]
                dp[s][i][j] += ((x + 1) * N / (i + j + k) + q) * (j + 1) / N
            if j - 1 >= 0 and k + 1 <= N:
                q = N**2 / ((i + j + k) ** 2)
                x = dp[s + 1][i][j - 1]
                dp[s][i][j] += ((x + 1) * N / (i + j + k) + q) * (k + 1) / N


print(*dp, sep="\n")
print(dp[0][0][0])
