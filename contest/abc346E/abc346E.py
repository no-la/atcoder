H, W, M = map(int, input().split())

# クエリを逆順で調べて、列、行の数を持っておけば良い
Q = [list(map(int, input().split())) for _ in range(M)]

columns = [True]*(W+1)
lines = [True]*(H+1)
c_count = W
l_count = H

from collections import defaultdict
d = defaultdict(int)
d[0] = W*H
for t, a, x in Q[::-1]:
    if t==1 and lines[a]:
        d[x] += c_count
        d[0] -= c_count
        l_count -= 1
        lines[a] = False
    elif t==2 and columns[a]:
        d[x] += l_count
        d[0] -= l_count
        c_count -= 1
        columns[a] = False

ans = [f"{i} {d[i]}" for i in range(200001) if d[i]>0]
print(len(ans))
print(*ans, sep="\n")