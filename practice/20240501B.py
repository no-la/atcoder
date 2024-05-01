N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
c = 0
d = dict()
for i in range(N):
    if c==K:
        break
    
    if A[i] not in d:
        c += 1
        d[A[i]] = 1


before = -1
for k in sorted(d.keys()):
    if k-before==1:
        before = k
    else:
        break
print(before+1)
