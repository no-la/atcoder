A, B, C, D, E, F = map(int, input().split())
MOD = 998244353

X = 1
for x in [A, B, C]:
    X *= x
    X %= MOD
Y = 1
for y in [D, E, F]:
    Y *= y
    Y %= MOD

print((X - Y) % MOD)
