N, K = map(int, input().split())
S = input()
MOD = 998244353

def f(s):
    # 長さKの回文かどうか
    return len(s)==K and s==s[::-1]

from collections import defaultdict
dp = [defaultdict(int) for _ in range(N+1)]
dp[0][""] = 1
# dp[i][s]: S[:i]が良い文字であり、末尾K-1文字がsになっている場合の数

for i in range(N):
    for k, v in dp[i].items():
        for c in "AB":
            if (S[i]==c or S[i]=="?") and not f(k+c):
                nk = (k+c)[-(K-1):]
                dp[i+1][nk] = (dp[i+1][nk] + v)%MOD

ans = 0
for v in dp[N].values():
    ans = (ans+v)%MOD
print(ans)
