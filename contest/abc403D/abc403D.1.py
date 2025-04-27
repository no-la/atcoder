import sys

input = lambda: sys.stdin.readline().rstrip()
N, D = map(int, input().split())
A = list(map(int, input().split()))
M = max(A) + 1


B = [0] * M
for a in A:
    B[a] += 1

if D == 0:
    print(sum([max(0, b - 1) for b in B]))
    exit()

seen = [False] * M
ans = 0

for i in range(M):
    if seen[i]:
        continue
    dp = [0, 0]
    j = i
    while j < M and not seen[j]:
        seen[j] = True
        dp = [dp[1], min(dp) + B[j]]
        j += D
    ans += min(dp)


print(ans)
