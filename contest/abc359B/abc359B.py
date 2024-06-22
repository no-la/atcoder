N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(2*N-2):
    ans += A[i]==A[i+2]

print(ans)
