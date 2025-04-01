import sys

input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]
MA = max(AB, key=lambda x: x[0])[0]
MB = max(AB, key=lambda x: x[1])[1]

d = [[0] * (MB + 1) for _ in range(MA + 1)]
# d[i][j]: 身長i、体重jの人数

for a, b in AB:
    d[a][b] += 1

cumsum = [[0] * (MB + 1) for _ in range(MA + 1)]
# cumsum[i][j]: 身長i以下、体重j以下の人数

for i in range(MA):
    for j in range(MB):
        cumsum[i + 1][j + 1] = (
            cumsum[i][j + 1] + cumsum[i + 1][j] - cumsum[i][j] + d[i + 1][j + 1]
        )

ans = 1
for c in range(1, MA + 1):
    a = min(MA, c + K)
    for d in range(1, MB + 1):
        b = min(MB, d + K)
        # 0 ** **
        # * cd cb
        # * ad ab
        ans = max(
            ans,
            cumsum[a][b] - cumsum[a][d - 1] - cumsum[c - 1][b] + cumsum[c - 1][d - 1],
        )

print(ans)
