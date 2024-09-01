N = int(input())
A = [input().split() for _ in range(N)]
INF = 10**10

ans = INF

for sl in range(100):
    for sr in range(100):
        temp = 0
        l = sl
        r = sr
        for i in range(N):
            a, s = A[i]
            a = int(a)-1
            if s=="L":
                temp += abs(a-l)
                l = a
            else:
                temp += abs(a-r)
                r = a
        ans = min(ans, temp)

print(ans)
