N, K = map(int, input().split())
A = set(map(int, input().split()))
B = []
for i in range(1, N+1):
    B.append(i)
    if i not in A:
        B.append(i)

ODD = [0]
EVEN = [0]
for i in range(0, len(B), 2):
    ODD.append(ODD[-1]+B[i])
for i in range(1, len(B), 2):
    EVEN.append(EVEN[-1]+B[i])
if K%2==0:
    print(EVEN[-1]-ODD[-1])
else:
    ans = 1000000000000000000
    for i in range(0,len(EVEN)):
        t = EVEN[i]-ODD[i]+(ODD[-1]-ODD[i+1])-(EVEN[-1]-EVEN[i])
        ans = min(ans, t)
    print(ans)