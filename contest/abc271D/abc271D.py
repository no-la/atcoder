N, S = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# DPの復元
dp = [[False] * (S + 1) for _ in range(N + 1)]
# dp[i][j]: A[:i]を使ってjを作れるかどうか
dp[0][0] = True

before = [[None] * (S + 1) for _ in range(N + 1)]
# before[i][j]: dp[i][j]がTrueのとき、直前に選んだカードの状態


for i in range(N):
    for j in range(S):
        if not dp[i][j]:
            continue
        ni = i + 1
        for s in [0, 1]:
            nj = j + A[i][s]
            if nj > S:
                continue
            dp[ni][nj] = True
            before[ni][nj] = s

# print(*dp, sep="\n")

if not dp[N][S]:
    print("No")
    exit()

ans = []
i = N
j = S
while before[i][j] is not None:
    s = before[i][j]
    ans.append("T" if s else "H")
    i -= 1
    j -= A[i][s]

print("Yes")
print(*ans[::-1], sep="")
