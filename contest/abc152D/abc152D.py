N = int(input())
SN = str(N)

def f(bl, br):
    # 正整数 bl...br でN以下のものの個数
    if bl=="0":
        return 0
    rv = 0
    if bl==br and int(br)<=N:
        rv += 1
    
    a = bl+br
    if int(a)>N:
        return rv
    na = bl+"0"+br
    while int(na)<=N:
        rv += 10**(len(a)-2)
        a = na
        na = na[:-1]+"0"+na[-1]
    
    k = len(a)
    if k==2:
        rv += 1
    else:
        l, r = 0, 10**(k-2)
        while l<r-1:
            c = (l+r)//2
            b = a[0]+("0"*k+str(c))[-k+2:]+a[-1]
            if int(b)<=N:
                l = c
            else:
                r = c
        rv += l+1
        # print(l, b)
    
    # print(a, rv)
    return rv
    

ans = 0
for a in range(1, N+1):
    sa = str(a)
    ans += f(sa[-1], sa[0])

print(ans)
