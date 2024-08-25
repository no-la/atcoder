N = int(input())
S = input()
MOD = 998244353
M = 10

def f(s):
    return ord(s)-ord("A")

dp = [[[0]*M for _ in range(2**M)] for _ in range(N+1)]
# dp[i][d][s]: S[:i]までで、dに含まれる種類のコンテストに出場し、最後はsである場合の数
# dはbitで管理する
# O(N * 2^M * M) ~ 1000 * 1000 * 10 = 10^7

# 配るDP
for i in range(N):
    for d in range(2**M):
        # 初めて参加するとき
        if not d:
            ns = f(S[i])
            nd = 1<<ns
            dp[i+1][nd][ns] += 1
            dp[i+1][nd][ns] %= MOD

        for s in range(M):
            # S[i]を選ばないとき
            dp[i+1][d][s] += dp[i][d][s]
            dp[i+1][d][s] %= MOD
            
            # S[i]を選ぶとき
            ns = f(S[i])
            nd = d|(1<<ns)
            if ns!=s and nd==d: # 条件を満たさない
                continue
            dp[i+1][nd][ns] += dp[i][d][s]
            dp[i+1][nd][ns] %= MOD
            

ans = 0
for d in range(1, 2**M):
    for s in range(M):
        ans += dp[N][d][s]
        ans %= MOD
print(ans)
