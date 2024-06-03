S = input()

ans = 0
for s in S:
    if s==s.upper():
        ans += 1
        break
for s in S:
    if s==s.lower():
        ans += 1
        break
if len(S)==len(set(S)):
    ans += 1

print("Yes" if ans==3 else "No")
