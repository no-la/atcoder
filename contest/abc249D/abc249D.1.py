N = int(input())
A = list(map(int, input().split()))
M = max(A)

d = [0]*(M+1)
# d[v]: v==A[i]なるiの個数
for a in A:
    d[a] += 1

ans = 0
# jを固定しkを探す
for vj in range(1, M+1):
    for vk in range(1, M//vj+1): # vj*vk == vi <= M
        vi = vj*vk
        ans += d[vi]*d[vj]*d[vk]

print(ans)
