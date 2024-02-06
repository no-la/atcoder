N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

M = min([Q[i]//A[i] if A[i]!=0 else 10000000 for i in range(N)])
ans = 0
for x in range(M, -1, -1):
    y = 100000000
    for i in range(N):
        xi = A[i]*x
        if xi>Q[i]:
            break
        if B[i]==0:
            continue
        yi = (Q[i]-xi)//B[i]
        if yi>=0:
            y = min(y, yi) #xを決めればyが定まる
        else:
            break
    else:
        ans = max(ans, x+y)
print(ans)