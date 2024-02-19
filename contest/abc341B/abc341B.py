N = int(input())
A = list(map(int, input().split()))

for i in range(N-1):
    s, t = map(int, input().split())
    A[i+1] += t * (A[i]//s)

print(A[-1])