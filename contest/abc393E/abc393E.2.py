import sys

input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())
A = list(map(int, input().split()))
M = max(A)

B = [0] * (M + 1)
# B[i]: iがAの元の倍数として何回現れるか
for a in A:
    B[a] += 1

C = [0] * (M + 1)
# C[i]: iがAの元の約数として何回現れるか
for i in range(1, M + 1):
    for j in range(i, M + 1, i):
        C[i] += B[j]

D = [0] * (M + 1)
# D[n]: A[i]=nの時の答え
for d in range(1, M + 1):
    if C[d] < K:
        continue
    for n in range(d, M + 1, d):
        D[n] = max(D[n], d)

for a in A:
    print(D[a])
