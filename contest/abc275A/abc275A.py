_ = int(input())
H = list(map(int, input().split()))
ans = 0
for i, h in enumerate(H):
    if h > H[ans]:
        ans = i

print(ans + 1)
