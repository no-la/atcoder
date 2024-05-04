S = input()
T = input()

i = 0
ans = []
for s in S:
    while i<len(T):
        if T[i]==s:
            ans.append(i+1)
            i += 1
            break
        i += 1

print(*ans)
