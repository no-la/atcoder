N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

for i in range(1, N):
    if A[i] != A[i-1]:
        print(A[i])
        break