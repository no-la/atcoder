N, M = map(int, input().split())
a = list(map(int, input().split()))

if M==0:
    print(1)
    exit()

a.sort()
if a[0]!=1:
    A = [0]+a
else:
    A = a
if A[-1]!=N:
    A.append(N+1)

INF = 10**18
k = min([A[i]-A[i-1]-1 for i in range(1, len(A)) if A[i]-A[i-1]>1]+[INF])

if k==INF:
    print(0)
    exit()

# print(k)
# print(A)
ans = 0
for i in range(1, len(A)):
    ans += -(-(A[i]-A[i-1]-1)//k)
print(ans)
