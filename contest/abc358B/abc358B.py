N, A = map(int, input().split())
T = list(map(int, input().split()))

now = 0
for t in T:
    if now<t:
        now = t+A
    else:
        now += A
    print(now)
