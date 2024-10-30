import math

N = int(input())
K = int(math.sqrt(N))
ans = 0
for i in range(1, K + 1):
    ans += (N // i - N // (i + 1)) * i
    if i <= N // (K + 1):
        ans += N // i

print(ans)
