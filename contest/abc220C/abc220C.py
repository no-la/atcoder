N = int(input())
A = list(map(int, input().split()))
X = int(input())

s = sum(A)
q = X//s
sm = s*q # s*q: X以下の最大のqの倍数

for i in range(N+1):
    if X<sm:
        break
    sm += A[i]

print(N*q+i)