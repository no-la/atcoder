S = input()

d = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = 0
j = 0
i = S.index(d[j])
while j + 1 < 26:
    ni = S.index(d[j + 1])
    ans += abs(ni - i)
    i = ni
    j += 1
print(ans)
