N = int(input())
S = input()

ans = {chr(ord("a")+i):0 for i in range(26)}
now = S[0]
count = 1
for i in range(1, N):
    if S[i]==now:
        count += 1
        continue
    ans[now] = max(ans[now], count)
    now = S[i]
    count = 1
ans[now] = max(ans[now], count)
print(sum(ans.values()))