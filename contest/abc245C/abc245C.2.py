N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

d = [0]*N
x = [A[0]]
i = 1
while i<N:
    # print(x)
    if (i==0 or d[i-1]==2) and d[i]==2:
        print("No")
        exit()
    
    if d[i]==2:
        x.pop()
        d[i] = 0
        i -= 1
        continue
    
    C = A if d[i]==0 else B
    d[i] += 1
    if i==0 or abs(x[i-1]-C[i])<=K:
        x.append(C[i])
        i += 1
        
# print(x)
print("Yes")
