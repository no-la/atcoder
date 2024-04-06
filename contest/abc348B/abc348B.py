N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    x1, y1 = A[i]
    ans = (0, 0)
    for j in range(N):
        if i==j:
            continue
        x2, y2 = A[j]
        ans = max(ans, ((x1-x2)**2+(y1-y2)**2, -j-1))
    print(-ans[1])