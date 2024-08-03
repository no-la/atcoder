N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

cs = 0
ans = 0
for i in range(N):
    # N-i個分だけx円にする
    x = (M-cs)//(N-i)
    x = max(x, A[i])
    x = min(x, A[-1])
    if cs+x*(N-i)<=M:
        ans = max(ans, x)
    cs += A[i]
    
print(ans if ans<A[-1] else "infinite")
    