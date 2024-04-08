Q = int(input())

from collections import defaultdict
d = defaultdict(int) # d[x]: xが何個あるか

querry = [list(map(int, input().split())) for _ in range(Q)]

# クエリを逆順に処理する
# 前準備
A = [x[0] for i, *x in querry if i==1]
for a in A:
    d[a] += 1

# removeをO(1)にする
A = set(A)
