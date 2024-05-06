N, M = map(int, input().split())

A = list(map(int, input().split()))[::-1]
C = list(map(int, input().split()))[::-1]

B = [None]*(M+1)
B[0] = C[0]//A[0]
for i in range(1, M+1):
    temp = 0
    for j in range(1,i+1):
        if not (0<=j<=N and 0<=i-j<=M):
            continue
        temp += A[j]*B[i-j]
    B[i] = (C[i]-temp)//A[0]

print(*B[::-1])
