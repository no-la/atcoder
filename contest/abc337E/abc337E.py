N = int(input())

l = 1
while l+1<N-(l+1)+1:
    l += 1
M = N-l

print(M)

for i in range(M):
    print(l, *list(range(i+1, i+1+l)))

S = input()
A = list(map(int, S))

d = [0]*N
for i in range(M):
    for j in range(i, i+l):
        d[j] += A[i]
ans = max([(d[i], i) for i in range(N)])
if ans[0]==0:
    ans = N
else:
    ans = ans[1]+1
print(ans)
