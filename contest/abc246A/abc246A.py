A = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    s = A[i]
    ans = [None, None]
    for j in range(1, 3):
        k = (i+j)%3
        if s[0]==A[k][0]:
            ans[1] = A[k][1]
        elif s[1]==A[k][1]:
            ans[0] = A[k][0]
    if ans[0]!=None and ans[1]!=None:
        print(*ans)
        exit()
        
        