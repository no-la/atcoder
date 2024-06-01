N, M, K = map(int, input().split())
d = []
s = []
for _ in range(M):
    C, *A, R = input().split()
    d.append(set(map(lambda x: int(x)-1, A)))
    s.append(R=="o")

# print(d)
# print(s)

# bit全探索
ans = 0
A = list(range(N))
N = len(A)
for i in range(2 ** N):
    keys = []
    for j in range(N):
        if not ((i >> j) & 1):
            continue
        keys.append(A[j])
    
    # keys が与えられた条件に矛盾しないか調べる
    for j in range(M):
        c = 0
        for k in keys:
            c += k in d[j]
        if (s[j] and c<K) or (not s[j] and c>=K):
            break
    else:
        ans += 1
print(ans)
