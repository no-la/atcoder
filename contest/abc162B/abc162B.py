N = int(input())

ans = 0
for i in range(1, N+1):
    a, b = i%3, i%5
    if a!=0 and b!=0:
        ans += i
print(ans)