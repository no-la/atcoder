N = int(input())
S = [input() for _ in range(N)]


from collections import defaultdict

d = defaultdict(int)
# d[s]: 文字列sの個数

# ローリングハッシュ...
# 覚えてない～～～～
# 勘で実装する

MOD = (1 << 61) - 1
B = 7


def char_hash(c):
    return ord(c) - ord("a") + 1


def debug():
    for T in S:
        my_hash = 0
        for i, t in enumerate(T):
            my_hash *= B
            my_hash %= MOD
            my_hash += char_hash(t)
            my_hash %= MOD
            print(T[: i + 1], "->", my_hash)


debug()

for T in S:
    my_hash = 0
    for t in T:
        my_hash *= B
        my_hash %= MOD
        my_hash += char_hash(t)
        my_hash %= MOD
        d[my_hash] += 1

for T in S:
    ans = 0
    my_hash = 0
    for i, t in enumerate(T):
        my_hash *= B
        my_hash %= MOD
        my_hash += char_hash(t)
        my_hash %= MOD
        if d[my_hash] > 1:
            ans = i + 1
    print(ans)
