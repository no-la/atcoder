N, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# imos法
imos = [0]*210000
#始点に+x, 終点の次の点に-xする
for s, t, p in A:
    imos[s] += p
    imos[t] -= p


# 適当な処理
for i in range(1, len(imos)):
    imos[i] += imos[i-1]
    
print("Yes" if max(imos)<=W else "No")