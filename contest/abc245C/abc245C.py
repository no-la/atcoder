N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

d = [0]*N
x = [A[0]]
i = 1
while i<N:
    print(x)
    if d[i]==0:
        d[i] = 1
        if not x and abs(x[i-1]-A[i])>K:
            x.pop()
            continue
        else:
            x.append(A[i])
            i += 1
    elif d[i]==1:
        d[i] = 2
        if not x and abs(x[i-1]-B[i])>K:
            x.pop()
            continue
        else:
            x.append(B[i])
            i += 1
    else:
        print("No")
        exit()

print("Yes")
