N = int(input())
P = list(map(int, input().split()))

# imos法
imos = [0] * N
# imos[i]: i回操作したときの喜ぶ人数

for i in range(N):
    l, r = (P[i] - 1 - i) % N, (P[i] + 1 - i) % N
    imos[l] += 1
    if r < l:
        imos[0] += 1

    if r + 1 < N:
        imos[r + 1] -= 1
    # print(P[i], l, r)

# 始点に+x, 終点の次の点に-xする
# 適当な処理
for i in range(1, len(imos)):
    imos[i] += imos[i - 1]

print(max(imos))
# print(imos)
