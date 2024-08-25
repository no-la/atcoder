N, K = map(int, input().split())
A = list(map(int, input().split()))
A = A[-K:] + A[:-K]

print(*A)
