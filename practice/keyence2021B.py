N, K = map(int, input().split())
A = list(map(int, input().split()))

d = [0]*(N+2)
for a in A:
    d[a] += 1

ans = 0
count = N
for i in range(N+2):
    if count>d[i]:
        ans += i*(count-d[i])
        count -= d[i]

print(ans)
