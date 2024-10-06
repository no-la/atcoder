N, X, M = map(int, input().split())

# 周期性
a = X
i = 0
first = [None] * M
cumsum = [None] * M
while first[a] is None:
    first[a] = i
    cumsum[i] = cumsum[i - 1] + a if i > 0 else a
    a = pow(a, 2, M)
    i += 1

loop_size = i - first[a]
loop_value = cumsum[i - 1] + a - cumsum[first[a]]

v1 = cumsum[first[a]]
v2 = loop_value * ((N - first[a] - 1) // loop_size)
v3 = cumsum[(N - first[a] - 1) % loop_size + first[a]] - cumsum[first[a]]
ans = v1 + v2 + v3

print(ans)
# print(first[a], i, loop_size, loop_value)
# print(v1, v2, v3)
