N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

print(A[0] + 2*sum(A[1:(N+1)//2]) - (A[(N+1)//2 - 1] if N%2 else 0))