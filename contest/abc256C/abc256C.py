temp = list(map(int, input().split()))
H = temp[:3]
W = temp[3:]

# 全探索？
d = [[] for _ in range(3)]
ans = 0
for h in range(3):
    for i in range(1, H[h]):
        for j in range(1, H[h]-i):
            k = H[h]-i-j
            if 1<=k:
                d[h].append((i,j,k))

# print(H, W, sep="\n")
# print(*d, sep="\n")

for a in d[0]:
    for b in d[1]:
        for c in d[2]:
            ans += all(
                a[i]+b[i]+c[i]==W[i] for i in range(3)
            )
print(ans)
