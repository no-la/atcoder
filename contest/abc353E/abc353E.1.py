N = int(input())
offset = "abc"
A = len(offset)
# S = input().split()
S = list(map(lambda s: offset+s, input().split()))


from collections import defaultdict
d = defaultdict(int)
for s in S:
    for i in range(A, len(s)):
        d[s[:i+1]] += 1

ans = 0

for i in range(N-1):
    s = S[i]
    for j in range(A, len(s)):
        d[s[:j+1]] -= 1
        ans += d[s[:j+1]]

print(ans)
