N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(i+1, N):
        y = A[j][1]-A[i][1]
        x = A[j][0]-A[i][0]
        if x!=0 and abs(y)<=abs(x):
            ans += 1
print(ans)
            
        