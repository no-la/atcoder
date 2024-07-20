N, K = map(int, input().split())
S = input()


def f(s):
    for i in range(N-K+1):
        s1 = s[i:i+K]
        s2 = s1[::-1]
        if s1==s2:
            # print(s, s[i:i+K])
            return False
    return True

seen = set()
ans = 0
# 順列 O(nPk)<=n!
import itertools
for l in itertools.permutations(S, N):
    s = "".join(l)
    if s in seen:
        continue
    seen.add(s)
    ans += f(s)
    # print(seen, ans)

print(ans)
