N, M = map(int, input().split())
A = [[] for _ in range(N)]
for i in range(M):
    temp = list(map(int, input().split()))[1:]
    for s in temp:
        A[s-1].append(i)    

P = list(map(int, input().split()))

# 全探索
# O(2^M * N*M)

ans = 0
# bit全探索
for i in range(2 ** N):
    d = [0]*M
    for j in range(N):
        if not ((i >> j) & 1):
            continue
        
        for s in A[j]:
            d[s] += 1
    for j in range(M):
        if d[j]%2 != P[j]:
            break
    else:
        ans += 1

print(ans)
