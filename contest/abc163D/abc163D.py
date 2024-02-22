mod = 10**9+7
N, K = map(int, input().split())

# K個選ぶときの和の場合の数の和を求めればよい
ans = 0
r = N
l = 0
for i in range(1, N+2):
    if i>=K:
        ans = (ans + r-l+1)%mod # [l, r]
    r += N-i
    l += i

print(ans)