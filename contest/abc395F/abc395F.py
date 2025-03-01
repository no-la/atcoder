import sys

input = lambda: sys.stdin.readline().rstrip()
N, X = map(int, input().split())
U = []
D = []
for i in range(N):
    u, d = map(int, input().split())
    U.append(u)
    D.append(d)


from heapq import heapify, heappop, heappush


ans = 0

# まず abs(U[i]-U[i+1]) <= X とする
hq = [(u, i) for i, u in enumerate(U)]
heapify(hq)
seen = [False] * N
while hq:
    u, i = heappop(hq)
    if seen[i]:
        continue
    seen[i] = True
    for d in [-1, 1]:
        j = i + d
        if j < 0 or j >= N:
            continue
        delta = U[j] - min(U[i] + X, U[j])
        U[j] -= delta
        ans += delta
        heappush(hq, (U[i], i))

# print(U, ans)

# 次は U[i]+D[i] = H とする
H = min([u + d for u, d in zip(U, D)])
ans += sum([u + d - H for u, d in zip(U, D)])

print(ans)
