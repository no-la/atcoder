a, b, C = map(int, input().split())

cn = C.bit_count()
cl = C.bit_length()

m = max((a, b, cl))
for k in range(m, 61):
    # Yを作る
    # k-a箇所だけCと同じ かつ 1をb個使う
    y = 0
    yc = 0 # yに1を使った回数
    xc = 0 # xに1が出て来る回数
    for i in range(k):
        if C&(1<<i) and yc<k-a: # C, yともに1
            y += 1<<i
            yc += 1
        else:
            if C&(1<<i): # Cは1, yは0
                xc += 1
            else: # Cは0, yは1
                if yc<b:
                    y += 1<<i
                    yc += 1
                else:
                    pass
        
    if yc==b and xc==a:
        print(y, C^y)
        exit()
print(-1)