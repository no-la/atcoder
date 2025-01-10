S = input()

ans = 0
digit = len(S) - 1
for s in S:
    ans += (ord(s) - ord("A") + 1) * (26**digit)
    digit -= 1

print(ans)
