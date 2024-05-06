N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

d = [0]*N
x = [A[0]]
i = 1
while i<N:
    # print(x)
    if d[i]==0:
        C = A
    elif d[i]==1:
        C = B
    else:
        print("No")
        exit()
        
    d[i] += 1
    if not x or abs(x[i-1]-C[i])<=K:
        x.append(C[i])
        i += 1
    elif d[i]==2:
        x.pop()
        if d[i-1]==2:
            print("No")
            exit()
        else:
            x.append(B[i-1])
            d[i-1] = 2
            d[i] = 0

print("Yes")
