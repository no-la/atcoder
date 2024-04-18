N, X = map(int, input().split())
S = input()

ans = X
for s in S:
    ans = max(0, ans+(1 if s=="o" else -1))
print(ans)