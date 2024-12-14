N, R = map(int, input().split())

t = [(1600, 2800), (1200, 2400)]
rate = R
for _ in range(N):
    d, a = map(int, input().split())
    d -= 1
    if t[d][0] <= rate < t[d][1]:
        rate += a

print(rate)
