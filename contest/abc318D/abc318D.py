import itertools
from collections import defaultdict

N = int(input())
D = [list(map(int, input().split())) for _ in range(N - 1)]


d = defaultdict(int)
# d[s]: 使った頂点がsのときの最大値

d[tuple()] = 0

for k in range(N):
    # 使っている頂点数がi
    # 重複なし組み合わせ O(nCk) 16C8~10^4
    for l in itertools.combinations(range(N), k):
        s = tuple(sorted(l))
        for i in range(N - 1):
            if i in s:
                continue
            for j in range(i + 1, N):
                if j in s:
                    continue
                ns = tuple(sorted(s + (i, j)))
                d[ns] = max(d[ns], d[s] + D[i][j - i - 1])

print(max(d.values()))
