S = input()
d = S.split("|")
ans = []
for s in d:
    ans.append(len(s))

print(*ans[1:-1])
