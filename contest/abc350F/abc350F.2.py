S = input()
N = len(S)

import sys
sys.setrecursionlimit(10**6)

d = [None]*N

imos = [0]*N
def f(si):
    i = si+1
    while i<N:
        if S[i]=="(":
            i = f(i)
        elif S[i]==")":
            d[si] = i
            d[i] = si
            imos[si] += 1
            imos[i] -= 1
            return i+1
        else:
            i += 1
    return N


j = 0
while j<N:
    if S[j]=="(":
        j = f(j)
    else:
        j += 1

for i in range(1, len(imos)):
    imos[i] += imos[i-1]

ans = []
def g(si, direction):
    i = si + direction
    while i<N:
        if direction==1:
            if S[i]=="(":
                i = g(i, -direction)
            elif S[i]==")":
                return i
            else:
                ans.append(S[i].swapcase() if imos[i]%2 else S[i])
                i += 1
        else:
            if S[i]==")":
                i = g(i, -direction)
            elif S[i]=="(":
                ans.append(S[i].swapcase() if imos[i]%2 else S[i])
                return i
            else:
                i -= 1
    return N

i = 0
while S[i]!="(":
    ans.append(S[i])
g(i, True)
print(*ans, sep="")
# print(imos)
# print(d)
