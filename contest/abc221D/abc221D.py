N = int(input())

from collections import defaultdict

# imos法
imos = defaultdict(int)
for _ in range(N):
    a, b = map(int, input().split())
    imos[a] += 1
    imos[a + b] -= 1

ans = [0] * (N + 1)
keys = sorted(imos.keys())
for i in range(len(keys) - 1):
    # imos[keys[-1]] = 0 なので、その分は ans に加算しなくてよい
    j, k = keys[i], keys[i + 1]
    imos[k] += imos[j]
    ans[imos[j]] += k - j

print(*ans[1:])
