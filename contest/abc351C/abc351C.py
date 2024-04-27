N = int(input())
A = list(map(int, input().split()))

d = []
for i in range(N):
    d.append(A[i])
    while True:
        if len(d)<=1:
            break
        if d[-1]!=d[-2]:
            break
        d.pop()
        d[-1] += 1
print(len(d))