N = int(input())

if N&1:
    print()
    exit()

dp = [set() for _ in range(N + 1)]
dp[2] = set(["()"])
# dp[i]: 長さiの正しいカッコ列のset

for i in range(4, N + 1, 2):
    for j in range(2, i):
        for s in dp[j]:
            for t in dp[i - j]:
                dp[i].add(f"{s}{t}")
                dp[i].add(f"{t}{s}")
    for s in dp[i - 2]:
        dp[i].add(f"({s})")

print(*sorted(dp[N]), sep="\n")
