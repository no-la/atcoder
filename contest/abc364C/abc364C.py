N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
ans = N
count = 0
for i, a in enumerate(A):
    count += a
    if count>X:
        ans = min(ans, i+1)

count = 0
for i, b in enumerate(B):
    count += b
    if count>Y:
        ans = min(ans, i+1)
print(ans)

