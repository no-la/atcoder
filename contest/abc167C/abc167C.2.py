# https://atcoder.jp/contests/abc167/submissions/50720944
N, M, X = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]


ans = 10**18

# bit全探索
for i in range(2 ** N):
    temp = [0]*M
    cost = 0
    for j in range(N):
        if not ((i >> j) & 1):
            continue
        cost += A[j][0]
        for k in range(1, M+1):
            temp[k-1] += A[j][k]
    if all([x>=X for x in temp]):
        ans = min(ans, cost)
        
print(ans if ans!=10**18 else -1)