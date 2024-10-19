N, C = map(int, input().split())
T = list(map(int, input().split()))
ans = 0
pre = -C
for i in range(N):
    if T[i] - pre >= C:
        pre = T[i]
        ans += 1
print(ans)
