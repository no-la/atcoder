N = int(input())
A = list(map(int, input().split()))
M = max(A)

d = [0]*(M+1)
# d[v]: v==A[i]なるiの個数
for a in A:
    d[a] += 1

ans = 0
# iを固定しj, kを探す
for vi in range(1, M+1):
    for vj in range(1, M+1): # vj*vk == vi <= M
        if vj**2>vi:
            break
        if vi%vj!=0:
            continue
        vk = vi//vj
        if vj==vk:
            ans += d[vi]*d[vj]*d[vk]
        else:
            ans += d[vi]*d[vj]*d[vk]*2

print(ans)
