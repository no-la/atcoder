N, T = map(int, input().split())
A = list(map(int, input().split()))

T %= sum(A)
now = 0
for i, a in enumerate(A):
    now += a
    if now >= T:
        print(i + 1, T - (now - a))
        exit()
