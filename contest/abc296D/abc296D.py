N, M = map(int, input().split())
INF = 10**15
ans = INF
for a in range(1, N+1):
    b = max(1, -(-M//a))
    # print(a, b)
    if b<a:
        break
    if not 1<=b<=N:
        continue
    
    ans = min(ans, a*b)

print(ans if ans<INF else -1)
    
