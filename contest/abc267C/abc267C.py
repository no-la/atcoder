N, M = map(int, input().split())
A = list(map(int, input().split()))

temp = 0
s = 0
for i in range(M):
    temp += (i + 1) * A[i]
    s += A[i]

ans = temp

for j in range(M, N):
    i = j - M
    temp -= A[i]
    s -= A[i]
    temp -= s
    temp += M * A[j]
    ans = max(ans, temp)
    s += A[j]
    # print(i, j, temp)

print(ans)
