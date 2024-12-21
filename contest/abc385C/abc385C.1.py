N = int(input())
H = list(map(int, input().split()))
M = max(H)

# 高さごとに、
# 幅の全探索＋尺取り

# 高さごとの尺取りで O(N)
# 幅の全探索で O(N)

towers = [[] for _ in range(M + 1)]
for i, h in enumerate(H):
    towers[h].append(i)

ans = 1
for l in towers:
    if not l:
        continue
    if len(l) == 1:
        ans = max(ans, 1)
        continue
    for delta in range(1, N):
        dp = [0] * (N + 1)
        # dp[i]: l[i]が最後のときの最長の要素数
        for i in range(1, len(l)):
            dp[i] = dp[i - 1] + 1 if l[i] - l[i - 1] == delta else 1
