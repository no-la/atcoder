Q = int(input())
A = []

for _ in range(Q):
    i, x = map(int, input().split())
    if i==1:
        A.append(x)
    else:
        print(A[-x])