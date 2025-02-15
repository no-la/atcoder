import sys

input = lambda: sys.stdin.readline().rstrip()
S = input()
N = len(S)
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if j - i != k - j:
                continue
            ans += (S[i], S[j], S[k]) == ("A", "B", "C")

print(ans)
