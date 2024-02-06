n = int(input())
digit = len(str(n))
before = 10
ans = "No"
for i in range(digit-1, -1, -1):
    r = 10**i
    m = n // r
    if m >= before:
        break
    before = m
    n %= r
else:
    ans = "Yes"

print(ans)