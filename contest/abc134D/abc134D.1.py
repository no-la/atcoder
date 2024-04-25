N = int(input())
A = list(map(int, input().split()))

d = [0]*(N+1)
ans = []

for i in range(N, 0, -1):
    if sum(d[i::i])%2!=A[i-1]:
        d[i] += 1
        ans.append(i)

print(len(ans))
if ans:
    print(*ans)




