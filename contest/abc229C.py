N, W = map(int, input().split())
AB = []
for i in range(N):
    AB.append(tuple(map(int, input().split())))
AB.sort()

ans = 0
m = 0
while AB:
    a, b = AB.pop()
    g = b if m+b<=W else W-m
    ans += a*g
    m += g
    if m==W:
        break
print(ans)