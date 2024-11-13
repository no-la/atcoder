N = int(input())
T = list(map(int, input().split()))
M = sum(T)

# ２グループに分けて総和の最大値を最小にする
d = set([0])
# d: 作れる数字のset

for i in range(N):
    for a in d.copy():
        d.add(a + T[i])

# print(d)
ans = min([max(M - a, a) for a in d])
print(ans)
