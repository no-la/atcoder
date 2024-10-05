import math

N, S, T = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(N)]

ans = 10**15
# 順列 O(nPk)<=n!
import itertools

for l in itertools.permutations(d, N):
    # bit全探索
    for i in range(2**N):
        temp = 0
        before = [0, 0]
        for j in range(N):
            sx, sy = l[j][:2]
            tx, ty = l[j][2:]
            if not ((i >> j) & 1):
                sx, tx = tx, sx
                sy, ty = ty, sy
            temp += math.sqrt((before[0] - sx) ** 2 + (before[1] - sy) ** 2) / S
            temp += math.sqrt((sx - tx) ** 2 + (sy - ty) ** 2) / T
            before = [tx, ty]
        ans = min(ans, temp)
        # print(temp)

print(ans)
