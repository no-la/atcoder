N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

i = 0
for k in range(N):
    j = k
    if i<j:
        i, j = j, i
    
    i = A[i][j]-1

print(i+1)
