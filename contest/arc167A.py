N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

k = N-M
ans = 0
for i in range(M):
    b = A.pop(0)
    if i<k:
        b += A.pop(0)
    ans += b*b
print(ans)