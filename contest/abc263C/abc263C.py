N, M = map(int, input().split())

ans = []
# 重複なし組み合わせ O(nCk)
import itertools
for l in itertools.combinations(range(1, M+1), N):
    ans.append(sorted(l))

ans.sort()

for l in ans:
    print(*l)
