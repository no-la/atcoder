S = input()
T = input()

ans = []
i = 0
for s in S:
    while s != T[i]:
        i += 1
    ans.append(i + 1)
    i += 1

print(*ans)
