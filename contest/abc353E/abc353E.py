N = int(input())
S = input().split()

from collections import defaultdict
d = defaultdict(int)
for s in S:
    for i in range(len(s)):
        d[s[:i+1]] += 1

ans = 0

for i in range(N-1):
    s = S[i]
    for j in range(1, len(s)+1):
        if d[s[:j]]<=1: # もう必要ない
            break
        d[s[:j]] -= 1
        ans += d[s[:j]]

print(ans)
