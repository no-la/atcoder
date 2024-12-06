from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
ans = 0
seen = [False] * N
for i in range(N):
    if seen[i]:
        continue
    seen[i] = True
    temp = A[i]
    j = i
    # <-
    while (A[(j - 1) % N] + 1) % M == A[j] or A[(j - 1) % N] == A[j]:
        j = (j - 1) % N
        if seen[j]:
            break
        seen[j] = True
        temp += A[j]
    j = i
    # ->
    while (A[(j + 1) % N] - 1) % M == A[j] or A[(j + 1) % N] == A[j]:
        j = (j + 1) % N
        if seen[j]:
            break
        seen[j] = True
        temp += A[j]

    # print(i, temp)
    ans = max(ans, temp)

# print(A, sum(A))
print(sum(A) - ans)
