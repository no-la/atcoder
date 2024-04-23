H, _ = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]


mn = 1000
for a in A:
    for b in a:
        mn = min(b, mn)

ans = 0
for a in A:
    for b in a:
        ans += b-mn
print(ans)
