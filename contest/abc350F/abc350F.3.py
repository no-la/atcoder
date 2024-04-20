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

i = 0
ans = []
direction = 1
to = []
while i<N:
    # print(i, to)
    if to and i==to[-1]:
        i = d[to.pop()]
        direction *= -1
        i += direction
        continue
    elif d[i]!=None:
        to.append(i)
        i = d[i]
        direction *= -1
    
    
    if S[i]!="(" and S[i]!=")":
        ans.append(S[i].swapcase() if imos[i]%2 else S[i])
    i += direction
        
print(*ans, sep="")
# print(imos)
# print(d)
