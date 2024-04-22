N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = 0
b = 0
for i in range(N):
    for j in range(N):
        a += (A[i]==B[j])
        b += (A[i]==B[j] and i==j)
print(b)
print(a-b)
