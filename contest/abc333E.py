N = int(input())
E = [list(map(int, input().split())) for _ in range(N)]

#Kで二分探索->違う!!!!!
left = 0
right = N
while left<right:
    print(left, right)
    c = (right-left)//2
    item = {}
    K = 0
    for i in range(N):
        t, x = E[i]
        if x not in item:
            item[x] = 0
        if t==1:
            item[x]+=1
            K+=1
        else:
            if item[x]==0:
                print(-1)
                exit()
            item[x]-=1
            K-=1
        if K>c:
            left = c
            break
    else:
        right = c

print(left)