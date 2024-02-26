N, Q = map(int, input().split())
A = list(map(int, input().split()))

from collections import defaultdict
d = defaultdict(list)
# d[x][i]: xがi回目に出てくる場所


# 事前に、Aのi番目の数字xが、何番目に出て来きたxかを調べておく
for i, a in enumerate(A):
    d[a].append(i+1)


for _ in range(Q):
    x, k = map(int, input().split())
    print(d[x][k-1] if k-1<len(d[x]) else -1)