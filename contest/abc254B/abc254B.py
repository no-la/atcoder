N = int(input())
A = []
for i in range(N):
    A.append([])
    for j in range(i+1):
        A[-1].append(1 if j==0 or j==i else A[i-1][j-1]+A[i-1][j])

for a in A:
    print(*a)
