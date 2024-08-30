A = list(map(int, input().split()))

ans = 0
for i in range(0, 101):
    if A[0]<=i<=A[1] and A[2]<=i<=A[3]:
        ans += 1
print(max(0, ans-1))
