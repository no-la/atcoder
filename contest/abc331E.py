N, M, L = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
CD = []
for _ in range(L):
    c, d = map(int, input().split())
    CD.append([A[c-1], B[d-1]])
A.sort(reverse=True)
B.sort(reverse=True)
CD.sort()

if not CD:
    print(A[0]+B[0])
    exit()
    
for r in range(N+M-1):
    ans = -1
    for i in range(r+1):
        a = A[i]
        b = B[r-i]
        if [a, b] == CD[-1]:
            CD.pop()
        else:
            ans = max(ans, a+b)
    if ans!=-1:
        print(ans)
        exit()