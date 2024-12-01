n, m = map(int, input().split())
a = []
for i in range(m):
    a_i = list(map(int, input().split()))
    a.append(a_i)
b = [0] * n
c = [[] for _ in range(n)]
for i in range(m):
    b[a[i][0] - 1] += 1
    b[a[i][1] - 1] += 1
    c[a[i][0] - 1].append(a[i][1])
    c[a[i][1] - 1].append(a[i][0])
for i in range(n):
    if b[i] == 0:
        print(0)
    else:
        print(b[i], end=" ")
        print(*sorted(c[i]))
