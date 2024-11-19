N, X = map(int, input().split())

ans = float("inf")
now = 0
for i in range(N):
    a, b = map(int, input().split())
    if X < i:
        continue
    ans = min(ans, now + a + b + (X - i - 1) * b)
    now += a + b

print(ans)
