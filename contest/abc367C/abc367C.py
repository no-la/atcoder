N, K = map(int, input().split())
R = list(map(int, input().split()))

d = [list(range(1, r+1)) for r in R]
ans = []
import itertools
for l in itertools.product(*d):
    if sum(l)%K==0:
        ans.append(l)

ans.sort()
for l in ans:
    print(*l)

if not ans:
    print()
