a, b, C = map(int, input().split())

cn = C.bit_count()
cl = C.bit_length()

# Yを作る
for i in range(1, 61): # i桁の2進数を調べる
    for j in range(i+1): # j箇所だけC, Yの同じ桁に1を使う
        y = 0
        for k in range(i): # 各桁を順に調べる
            cis1 = C&(1<<k)
            if cis1 and y.bit_count()<j:
                y += 1<<k
            
            if y.bit_count()==j:
                break
        else:
            continue
                
        for k in range(i): # 各桁を順に調べる
            cis1 = C&(1<<k)
            if (not cis1) and y.bit_count()<b:
                y += 1<<k
                
        x = C^y # x^y = C -> x^y^y = C^y -> x = C^y
        if x.bit_count()==a and y.bit_count()==b:
            print(x, y)
            exit()
                
print(-1)