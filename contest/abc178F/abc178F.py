N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


DA = [None]*(N+1) # DA[i]: A[DA[i][0]: DA[i][1]]がiである
DB = [None]*(N+1) # 同上
i = 0
while i<N:
    pre = A[i]
    l = i
    r = i
    while r<N and A[r]==pre:
        r += 1
    DA[A[l]] = (l, r)
    i = r
i = 0
while i<N:
    pre = B[i]
    l = i
    r = i
    while r<N and B[r]==pre:
        r += 1
    DB[B[l]] = (l, r)
    i = r
    
# print(DA)
# print(DB)

imos = [0]*N # 
#始点に+x, 終点の次の点に-xする
for i in range(N):
    if DA[i] is None:
        continue
    l, r = DA[i]
    imos[l] += l
    imos[r] += 1
    
# 適当な処理
for i in range(1, len(imos)):
    imos[i] += imos[i-1]
    