N = int(input())
A = list(map(int, input().split()))
M = 2 * N + 1

ans = [0] * (M + 1)
for i, a in enumerate(A):
    j = i + 1
    for na in [2 * j, 2 * j + 1]:
        if not (1 <= na <= M):
            continue
        ans[na] = ans[a] + 1

print(*ans[1:], sep="\n")
