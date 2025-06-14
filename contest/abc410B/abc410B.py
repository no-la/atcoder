import sys

input = lambda: sys.stdin.readline().rstrip()
N, Q = map(int, input().split())
X = list(map(int, input().split()))

hako = [0] * N
ans = []

for i in range(Q):
    if X[i] > 0:
        hako[X[i] - 1] += 1
        ans.append(X[i])
    else:
        j = 0
        for k, a in enumerate(hako):
            if hako[j] > a:
                j = k
        hako[j] += 1
        ans.append(j + 1)

print(*ans)
