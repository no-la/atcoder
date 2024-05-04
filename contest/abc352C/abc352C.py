N = int(input())
A = []
B = []
sa = 0
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    sa += a

ans = 0
for i in range(N):
    ans = max(ans, sa-A[i]+B[i])

print(ans)
