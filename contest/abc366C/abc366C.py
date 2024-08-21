Q = int(input())

N = 10**6
d = [0]*(N+1)
count = 0

for _ in range(Q):
    t = list(map(int, input().split()))
    if t[0]==1:
        x = t[1]
        d[x] += 1
        if d[x]==1:
            count += 1
    elif t[0]==2:
        x = t[1]
        d[x] -= 1
        if d[x]==0:
            count -= 1
    elif t[0]==3:
        print(count)

