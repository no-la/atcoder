N, K = map(int, input().split())
A = list(map(int, input().split()))

d = [0]*N
for a in A:
    d[a] += 1

ans = 0
count = K
for i in range(N):
    print(ans, count)
    if count>d[i]:
        ans += i*(count-d[i])
        count = d[i]

print(ans)
