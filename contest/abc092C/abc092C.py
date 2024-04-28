N = int(input())
A = [0] + list(map(int, input().split())) + [0]

s = 0
for i in range(0, N+1):
    s += abs(A[i+1]-A[i])
    
for i in range(1, N+1):
    l, r = sorted([A[i-1], A[i+1]])
    if l<=A[i]<=r:
        ans = s
    elif A[i]<l:
        ans = s-abs((A[i]-l)*2)
    elif A[i]>r:
        ans = s-abs((A[i]-r)*2)
    
    print(ans)
        
