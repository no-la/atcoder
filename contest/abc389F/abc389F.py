N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = max(A)

d = [None] * (M + 1)
# d[i]: 最初にiの時の答え

l = 1
while l < N:
    # lが最終何になるか調べる
    ...


Q = int(input())
for _ in range(Q):
    X = int(input())
