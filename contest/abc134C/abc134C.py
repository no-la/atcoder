N = int(input())
A = [int(input()) for _ in range(N)]

B = A.copy()
B.sort()

for i in range(N):
    j = -1
    if B[j]==A[i]:
        j -= 1
    print(B[j])
