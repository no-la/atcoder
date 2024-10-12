from collections import defaultdict

S = input()
N = len(S)

cumsum = defaultdict(lambda: [0] * (N + 1))
# cumsum[s][i]: S[:i]までにsが何回現れるか
for s in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    for i in range(N):
        cumsum[s][i + 1] = cumsum[s][i] + (S[i] == s)

ans = 0
for i in range(N):
    for s in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        l = cumsum[s][i]
        r = cumsum[s][-1] - cumsum[s][i + 1]
        ans += l * r

print(ans)
