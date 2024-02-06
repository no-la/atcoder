S = list(input())
S.sort(reverse=True)

ans = "z"
c = 0
for s in S:
    if ans==s:
        continue
    d = S.count(s)
    if c<=d:
        c = d
        ans = s
print(ans)