N = int(input())
d = [list(map(int, input().split())) for _ in range(N)]

# 決め打ち二分探索
l, r = 0, 10**15
while l<r-1: # lは取り得ない値、rは取り得る値
    c = (l+r)//2
    query = []
    for i in range(N):
        h, s = d[i]
        query.append((c-h)//s)
    
    query.sort()
       
    for i in range(N):
        if query[i]<i:
            l = c
            break
    else:
        r = c

print(r)
