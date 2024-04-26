N, C = map(int, input().split())

from collections import defaultdict
d = defaultdict(int)
# imos法
# imos = [0]*N
#始点に+x, 終点の次の点に-xする
for _ in range(N):
    a, b, c = map(int, input().split())
    # imos[a-1] += c
    # imos[b-1] += c
    d[a-1] += c
    d[b] -= c

# 適当な処理
k = sorted(d.keys())
before = k[0]
for i in k[1:]:
    d[i] += d[before]
    before = i
# for i in range(1, len(imos)):
    # imos[i] += imos[i-1]

ans = 0
before = k[0]
for i in k[1:]:
    # print(d[before], before, "->", i)
    ans += (i-before)*min(C, d[before])
    before = i
print(ans)



