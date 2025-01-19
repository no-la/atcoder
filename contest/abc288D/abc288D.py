N, K = map(int, input().split())
A = list(map(int, input().split()))

# mod K で分類して、グループごとに累積和
d = [[0] * (N + 1) for _ in range(K)]
# d[i][j]: sum(A[i:j:K])
for i in range(K):
    for j in range(N):
        if j % K == i:
            d[i][j + 1] = d[i][j] + A[j]
        else:
            d[i][j + 1] = d[i][j]

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    L -= 1
    tail_K = [d[i][R] - d[i][L] for i in range(K)]

    print("Yes" if len(set(tail_K)) == 1 else "No")
