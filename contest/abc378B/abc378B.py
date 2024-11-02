N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())

for _ in range(Q):
    t, d = map(int, input().split())
    t -= 1
    q, r = A[t]
    for i in range(-3, 3):
        temp = ((d // q) + i) * q + r
        if temp >= d:
            print(temp)
            break
