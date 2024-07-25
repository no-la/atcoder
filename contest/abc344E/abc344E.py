N = int(input())
A = list(map(int, input().split()))
Q = int(input())

# 辺をもっておく
from collections import defaultdict
left = defaultdict(lambda:None)
right = defaultdict(lambda:None)

for i in range(N-1):
    left[A[i+1]] = A[i]
    right[A[i]] = A[i+1]

left[-1] = A[-1]
right[A[-1]] = -1
left[A[0]] = 0
right[0] = A[0]
for _ in range(Q):
    t, *x = map(int, input().split())
    if t==1:
        x, y = x
        z = right[x]
        right[x] = y
        left[z] = y
        right[y] = z
        left[y] = x
        # print(x, z, "->", x, y, z)
    else:
        y = x[0]
        x = left[y]
        z = right[y]
        left[z] = x
        right[x] = z
        del left[y]
        del right[y]
        # print(x, y, z, "->", x, z)
    # print(left)
    # print(right)

ans = []
v = right[0]
while v!=-1:
    ans.append(v)
    v = right[v]
print(*ans)
