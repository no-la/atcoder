A = list(map(int, input().split()))
ans = 0
for i in range(1, 5):
    ans += A.count(i) // 2
print(ans)
