import math

R = int(input())


# 良い感じに一方向を考えて4倍する感じ
# 右上方向を考える
c1 = 0
for x in range(R):
    if x + 0.5 > R:
        continue
    a = (x + 0.5) ** 2 - R**2
    y = math.floor((-1 + math.sqrt(1 - 4 * a)) / 2)
    c1 += y
    # print(x, y)

# 中心だけまだ数えてない
ans = 4 * c1 + 1
print(ans)
