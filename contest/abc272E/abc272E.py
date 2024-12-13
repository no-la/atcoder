N, M = map(int, input().split())
A = list(map(int, input().split()))

# 見ておくべき数字は 0,1,2,..., N だけ
# A[i]がそこにはいるのは、1-indexedでN/i回だけ
# N + N/2 + N/3 + ... + N/N = N(1 + 1/2 + 1/3 + ... + 1/N)
# これはO(NlogN)

d = [set() for _ in range(M + 1)]
# d[i]: i回操作後に存在する数字

for i, a in enumerate(A):
    start = max(0, -(a // (i + 1)))
    end = min(M + 1, (N - a) // (i + 1) + 1)
    for j in range(start, end):
        if a + (j * (i + 1)) > N:
            break
        d[j].add(a + (j * (i + 1)))

# print(d)

for i in range(1, M + 1):
    for j in range(N + 1):
        if j not in d[i]:
            print(j)
            break
