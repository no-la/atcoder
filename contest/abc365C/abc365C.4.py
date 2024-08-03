N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
A = [0]+A
ans = 0
cs = 0
for i in range(1, N+1):
    # A[:i]だけをそのままの金額にする場合
    cs += A[i-1]
    x = (M-cs)//(N-i+1)
    
    if A[i-1]<= x:
        ans = max(ans, x)

print(ans if ans<A[-1] else "infinite")
    