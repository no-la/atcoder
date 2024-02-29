N, M, X = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 全探索
ans = 10**18
# 重複なし組み合わせ O(nCk)
import itertools
for n in range(1, N+1):
    for l in itertools.combinations(range(N), n):
        a = [0]*M
        for i in l:
            for j in range(M):
                a[j] += A[i][j+1]
        if all([a[k]>=X for k in range(M)]):
            ans = min(ans, sum([A[k][0] for k in l]))
print(ans if ans!=10**18 else -1)