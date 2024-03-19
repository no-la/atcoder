N = int(input())
A = list(map(int, input().split()))

if 0 in A:
    print(0)
    exit()
    
INF = 10**18

ans = 1
for a in A:
    if INF<ans*a:
        ans = -1
        break
    ans *= a
print(ans)