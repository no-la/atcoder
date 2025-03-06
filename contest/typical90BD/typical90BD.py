import sys

input = lambda: sys.stdin.readline().rstrip()
N, S = map(int, input().split())

dp = [[False] * (S + 1) for _ in range(N + 1)]
# dp[i][j]: i番目まで見てjになるかどうか
dp[0][0] = True

pre = [[None]*(S+1) for _ in range(N+1)]
# pre[i][j]: dp[i][j]の直前の(j, A(or B))

for i in range(N):
    a, b = map(int, input().split())
    for j in range(S+1):
        if not dp[i][j]:
            continue
        for k in range(2):
            x = [a, b][k]
            y = ["A", "B"][k]
            nj = j + x
            if nj > S:
                continue
            dp[i+1][nj] |= dp[i][j]
            pre[i+1][nj] = (j, y)

if not dp[N][S]:
    print("Impossible")
    exit()

ans = []
i = N
j = S
while i > 0:
    ans.append(pre[i][j][1])
    j = pre[i][j][0]
    i -= 1

# print(*pre, sep="\n")
print(*ans[::-1], sep="")