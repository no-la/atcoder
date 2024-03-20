N = list(input())
n = len(N)

ans = 0
# 11! ~ 4*10^7
# 順列 O(nPk)<=n!
import itertools
for l in itertools.permutations(N, n):
    for i in range(1, n):
        if l[0]=="0" or l[i]=="0":
            continue
        ans = max(ans, int("".join(l[:i])) * int("".join(l[i:])))

print(ans)