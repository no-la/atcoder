N = int(input())
S = [input() for _ in range(N)]


from collections import defaultdict

d = defaultdict(int)
# d[s]: 文字列sの個数

# ローリングハッシュ...
# 覚えてない～～～～
# 勘で実装する

for s in S:
    for i in range(len(s)):
        d[s[: i + 1]] += 1

MOD = [
    (1 << 61) - 1,
    998244353,
]
B = [7, 61]


def char_hash(c):
    return ord(c) - ord("a") + 1


for T in S:
    my_hash = [0, 0]
    for t in T:
        for k in range(len(B)):
            my_hash[k] *= B[k]
            my_hash[k] %= MOD[k]
            my_hash[k] += char_hash(t)
            my_hash[k] %= MOD[k]
        d[tuple(my_hash)] += 1

for T in S:
    ans = 0
    my_hash = [0, 0]
    for i, t in enumerate(T):
        for k in range(len(B)):
            my_hash[k] *= B[k]
            my_hash[k] %= MOD[k]
            my_hash[k] += char_hash(t)
            my_hash[k] %= MOD[k]
        if d[tuple(my_hash)] > 1:
            ans = i + 1
    print(ans)
