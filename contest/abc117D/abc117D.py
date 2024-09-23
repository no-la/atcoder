"""AC"""

N, K = map(int, input().split())
A = list(map(int, input().split()))

# 桁ごとに最大化する
M = 40
ans_x = 0
for i in range(M, -1, -1):
    x = 1 << i
    if ans_x + x > K:
        continue
    count = [0, 0]
    for a in A:
        count[(a & x) == 0] += 1

    ans_x += x if count[1] > count[0] else 0
    # print(i, x, count, ans_x)


ans = sum([ans_x ^ a for a in A])
print(ans)
