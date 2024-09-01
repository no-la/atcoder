A, B = map(int, input().split())

ans = set()

import itertools
for x in range(-98, 200):
    # 順列 O(nPk)<=n!
    for l in itertools.permutations([A, B, x], 3):
        p, q, r = l
        if q-p == r-q:
            ans.add(x)

print(len(ans))
