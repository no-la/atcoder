N, X = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dp = [[False] * (X + 1) for _ in range(N + 1)]
# dp[i][j]: A[:i]からj円を作れるかどうか

dp[0][0] = True
for i in range(N):
    for j in range(X + 1):
        if not dp[i][j]:
            continue
        a = A[i][0]
        for b in range(A[i][1] + 1):
            nj = j + a * b
            if nj > X:
                break
            dp[i + 1][nj] = True

print("Yes" if dp[N][X] else "No")
