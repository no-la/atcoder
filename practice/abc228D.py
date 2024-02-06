N = 2**20
A = [-1]*N
Q = int(input())
goto = [(i+1)%N for i in range(N)]
for _ in range(Q):
    t, x = map(int, input().split())
    if t==1:
        h = x%N
        tmp = []
        while A[h]!=-1:
            tmp.append(h)
            h=goto[h]
        A[h]=x
        for i in tmp:
            goto[i]=h
    else:
        print(A[x%N])