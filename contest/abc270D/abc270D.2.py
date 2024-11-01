N, K = map(int, input().split())
A = list(map(int, input().split()))

d = [[0, 0] for _ in range(N + 1)]
# d[i]: 山の残りがiから始めたときの答え

for i in range(1, N + 1):
    for k in range(K):
        if i < A[k]:
            break
        temp = d[i - A[k]].copy()
        temp[1], temp[0] = temp[0], temp[1]
        temp[0] += A[k]
        d[i] = max(d[i], temp)

print(d[N][0])
# print(*d, sep="\n")
