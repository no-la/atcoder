N = int(input())
from collections import defaultdict
d = defaultdict(list)
for _ in range(N):
    x, c = map(int, input().split())
    d[c].append(x)

for k in d:
    d[k].sort()

d = [(0, [0])] + sorted(d.items()) + [(10**9+1, [0])]
# print(*d)

dp = [[0, 0] for _ in range(len(d))]
# dp[i][j]: 色iまでを回収し終えた状態でd[i][-j]にいるときの最小時間
for i in range(1, len(d)):
    for j in range(2):
        temp = 10**16
        to1 = d[i][1][j-1]
        to2 = d[i][1][-j]
        for k in range(2):
            now = dp[i-1][k]
            from_ = d[i-1][1][-k]
            temp = min(temp, now+abs(to1-from_)+abs(to2-to1))
        dp[i][j] = temp

# print(*d)
# print(*dp)
print(dp[-1][0])
