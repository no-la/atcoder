N, K, C = map(int, input().split())
S = input()

# 独立に考えられる区間ごとに「働ける最大日数」を調べる
D = S.split("x"*C)
ans = []
for d in D:
    i = 0
    count = set()
    while i<len(d):
        if d[i]=="o":
            count.add(i+1)
            i += C
        else:
            i += 1
    ans.append(count)

if sum([len(a) for a in ans])>N:
    print()
else:
    pass
        
