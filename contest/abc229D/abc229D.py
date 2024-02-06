S = input()
K = int(input())

b = False
d = [] #.のみからなる部分文字列がS[d[_][0]:d[_][1]]になる
for i in range(len(S)):
    if S[i]==".":
        if not b:
            d.append([i])
            b = True
    else:
        if b:
            d[-1].append(i)
            b = False
if b:
    d[-1].append(i+1)
    
ans = 0
s = 0
count = d[s][1]-d[s][0]
for i in range(1, len(d)):
    l = d[i][1]-d[i][0]
    if count+l>K:
        ans = max(ans, s+d[i][0]+K-count)
        s = d[i+1][0]
    else:
        ans = max(ans, i-s)
        

    
