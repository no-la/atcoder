N, M, T = map(int, input().split())

now = N
pre = 0
for _ in range(M):
    a, b = map(int, input().split())
    now -= a-pre
    if now<=0:
        print("No")
        exit()
    
    pre = b
    now = min(now+b-a, N)

print("Yes" if now>T-pre else "No")
