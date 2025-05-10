import sys, math

input = lambda: sys.stdin.readline().rstrip()
A, O, B, G = map(int, input().split())
S = A + O + B + G
MOD = 998244353

ans = 0

for i in range(G, G + B + 1):
    # 一番左のブドウが、右から数えてi番目にあるとき

    # まずバナナの配置
    temp = math.comb(G, i - G) % MOD

    # リンゴを置いて、オレンジを置く
    temp *= math.comb(S - i, O) % MOD

    ans += temp
    ans %= MOD
print(ans)
