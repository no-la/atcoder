S = input()

d = {"A", "T", "G", "C"}
c = 0
ans = 0
for s in S:
    if s in d:
        c += 1
        ans = max(ans, c)
    else:
        c = 0
print(ans)