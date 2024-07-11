N = int(input())

dp = [N]*(N+1)
dp[0] = 0
dp[1] = 1
# dp[i]: i本のジュースに腐っているものがあるか、あるならどれかがわかる最小の人数
for i in range(2, N+1):
    for j in range(i+1):
        if i<j:
            break
        dp[i] = min(dp[i], dp[j]+dp[i-j])

print(dp)

