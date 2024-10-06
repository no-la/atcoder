N, X, M = map(int, input().split())

# 周期性
a = X
i = 0
first = [None] * M
first[a] = 0
cumsum = [0] * M
cumsum[0] = X
while first[pow(a, 2, M)] is None:
    a = pow(a, 2, M)
    i += 1
    first[a] = i
    cumsum[i] = cumsum[i - 1] + a

loop_size = i - first[a] + 1
loop_value = cumsum[i] + pow(a, 2, M) - cumsum[first[a]]

ans = cumsum[i]
ans += loop_value * ((N - first[a] - 1) // loop_size)
ans += cumsum[(N - first[a] - 1) % loop_size + first[a] - 1] - cumsum[first[a] - 1]

print(ans)
print(cumsum)
print(first[a], i, loop_size, loop_value)
print(cumsum[i])
print(loop_value * ((N - first[a] - 1) // loop_size))
print(cumsum[(N - first[a] - 1) % loop_size + first[a] - 1] - cumsum[first[a] - 1])
