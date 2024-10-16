N = int(input())

d = [None] * (N + 1)
# d[i]: 残りiターンのときのスコアの期待値

d[0] = 0
for i in range(N):
    d[i + 1] = sum([max(n, d[i]) for n in range(1, 7)]) / 6

print(d[N])
