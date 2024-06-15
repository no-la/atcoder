N, M = map(int, input().split())
S = [input() for _ in range(N)]

# 売り場で全探索
# 2^N <= 1024

ans = N
# bit全探索
for i in range(2 ** N):
    check = [False]*M
    for j in range(N):
        if not ((i >> j) & 1):
            continue
        
        for k in range(M):
            if S[j][k]=="o":
                check[k] = True
    if all(check):
        ans = min(ans, i.bit_count())

print(ans)
