S = input()
N = len(S)

d = [None]*N

imos = [0]*N

left = []
for i in range(N):
    if S[i]=="(":
        left.append(i)
    elif S[i]==")":
        l = left.pop()
        r = i
        imos[l] += 1
        imos[r] -= 1
        d[l] = r
        d[r]  = l


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
