N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(lambda x: int(x) - 1, input().split()))
A.append(N + 1)

for i in L:
    if A[i] + 1 < A[i + 1]:
        A[i] += 1

print(*A[:-1])
