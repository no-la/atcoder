K = int(input())

from collections import defaultdict

d = defaultdict(int)

temp = K
for i in range(2, K + 1):
    if i * i > K:
        break
    while temp % i == 0:
        d[i] += 1
        temp //= i

if temp > 1:
    d[temp] += 1

ans = 0
for k, v in d.items():  # O(logK)
    k_count = 0
    i = k
    while k_count < v:
        temp = i
        while temp % k == 0:
            temp //= k
            k_count += 1
        i += k
    ans = max(ans, i - k)
print(ans)
