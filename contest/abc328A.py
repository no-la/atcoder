N, X = map(int, input().split())
S = list(map(int, input().split()))

ans = 0
for i in S:
    if i <= X:
        ans += i

print(ans)