N, M = map(int, input().split())
H = list(map(int, input().split()))

ans = 0
i = 0
while i<N:
    M -= H[i]
    i += 1
    ans += (M>=0)

print(ans)
