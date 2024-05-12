N = int(input())
S = input().split()

B = 200
MOD = 10**16+61

from collections import defaultdict
d = defaultdict(int)
for s in S:
    hash_ = 0
    for i in range(len(s)):
        hash_ = (hash_*B+ ord(s[i]))%MOD
        d[hash_] += 1

ans = 0

for i in range(N-1):
    s = S[i]
    hash_ = 0
    for j in range(len(s)):
        hash_ = (hash_*B+ ord(s[j]))%MOD
        d[hash_] -= 1
        ans += d[hash_]

print(ans)
