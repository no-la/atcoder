N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

t = sum([a/b for a, b in A])/2
c = 0
i = 0
while t>c+A[i][0]/A[i][1]:
    c += A[i][0]/A[i][1]
    i += 1
offset = sum([A[j][0] for j in range(i)])
print(offset + (t-c)*A[i][1])