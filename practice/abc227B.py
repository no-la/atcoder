N = int(input())
S = list(map(int, input().split()))

data = [False]*(1001)
for a in range(1, 200):
    for b in range(1, 200):
        t = 4*a*b+3*a+3*b
        if t <= 1000:
            data[t] = True

ans = 0
for s in S:
    if not data[s]:
        ans += 1

print(ans)