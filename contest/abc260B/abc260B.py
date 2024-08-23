N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = [(A[i]+B[i], -i) for i in range(N)]
A = [(A[i], -i) for i in range(N)]
B = [(B[i], -i) for i in range(N)]

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

seen = [False]*N
ans = []
c = 0
i = 0
while c<X:
    j = -A[i][1]
    if not seen[j]:
        ans.append(j+1)
        seen[j] = True
        c += 1
    i += 1

c = 0
i = 0
while c<Y:
    j = -B[i][1]
    if not seen[j]:
        ans.append(j+1)
        seen[j] = True
        c += 1
    i += 1

c = 0
i = 0
while c<Z:
    j = -C[i][1]
    if not seen[j]:
        ans.append(j+1)
        seen[j] = True
        c += 1
    i += 1

print(*sorted(ans), sep="\n")
# print(*C, sep="\n")
