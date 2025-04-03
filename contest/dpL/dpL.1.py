import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
A = list(map(int, input().split()))
M = (N + 1) * (N + 2) // 2 + 1

# あり得る盤面は 1+2+...+N~N^2 通り
dp = [0] * M
# dp[k]: k で表される盤面でのX-Y の値

for i in range(N):
    for j in range(i + 1):
        k = (i**2 + i) // 2 + j
        l, r = j, N - (i - j) - 1
        f = max if i & 1 == 0 else min
        # いま、A[l: r+1] が残っている
        # A[l]かA[r] を取り除く
        for dk, x in [(i + 1, l), (i + 2, r)]:
            nk = k + dk
            dp[nk] = f(dp[nk], dp[k] + A[x] if i & 1 == 0 else dp[k] - A[x])


# 盤面の遷移がつくれたので、シミュレーションする
now = 0
for i in range(N):
    nl, nr = now + (i + 1), now + (i + 2)
    if i & 1 == 0:
        if dp[nl] > dp[nr]:
            now = nl
        else:
            now = nr
    else:
        if dp[nl] < dp[nr]:
            now = nl
        else:
            now = nr

print(dp)
print(dp[now])
