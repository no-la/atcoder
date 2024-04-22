N, X = map(int, input().split())
T = input()
S = [T[0]]
i = 1
while i<N:
    if not S:
        S.append(T[i])
    elif S[-1] in ("L", "R") and T[i]=="U":
        S.pop()
    else:
        S.append(T[i])
    i += 1


now = X
for s in S:
    # print(now)
    if s=="U":
        now = now>>1
    elif s=="L":
        now = now<<1
    else:
        now = (now<<1) + 1
print(now)
