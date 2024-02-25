N = int(input())
A = list(map(int, input().split()))

cs = [0]*(N+1)
for i in range(N):
    cs[A[i]] += 1

d = [v*(v-1)//2 for v in cs]
csd = [0]*(N+1)
csd[0] = d[0]
for i in range(1, N+1):
    csd[i] = csd[i-1] + d[i]

for i in range(N):
    v = cs[A[i]]
    print(csd[A[i]-1] + (v-1)*(v-2)//2 + csd[-1]-csd[A[i]])