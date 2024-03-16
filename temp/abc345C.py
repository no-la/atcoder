S = input()
N = len(S)

d = {s:0 for s in "abcdefghijklmnopqrstuvwxyz"}
b = False
ans = 0
for i in range(N):
    d[S[i]] += 1
    ans += N-1 - i
    if d[S[i]]==2:
        b = True
    if b:
        ans -= 1
print(ans)