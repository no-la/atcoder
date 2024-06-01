N, L, R = map(int, input().split())
L -= 1
R -= 1
A = list(range(1, N+1))
print(*A[:L], *A[L:R+1][::-1], *A[R+1:])

