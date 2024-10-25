N = int(input())

A = [i for i in range(61) if N & (1 << i)]

ans = []
# bit全探索
M = len(A)
for i in range(2**M):
    temp = 0
    for j in range(M):
        if not ((i >> j) & 1):
            continue
        temp += 1 << A[j]
    ans.append(temp)

print(*sorted(ans), sep="\n")
