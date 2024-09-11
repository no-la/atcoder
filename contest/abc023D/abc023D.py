N = int(input())
d = [list(map(int, input().split())) for _ in range(N)]

# 決め打ち二分探索
l, r = min([a for a, _ in d])-1, 10**15
while l<r-1: # lは取り得ない値、rは取り得る値
    c = (l+r)//2
    until = [0]*N
    for i in range(N):
        h, s = d[i]
        if (c-h)//s<0:
            l = c
            break
        until[min(N-1, (c-h)//s)] += 1
    else:
        count = 0
        for i in range(N):
            count += until[i]
            if count>i+1:
                l = c
                break
        else:
            r = c

print(r)
