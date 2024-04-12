N = int(input())
A = list(map(int, input().split()))


d = [0]*(N+1)
e = [0]*(N+1) # e[i]: d[:i+1]の最大値
for i in range(1, N+1):
    d[i] = d[i-1]+A[i-1]
    e[i] = max(e[i-1], d[i])


# 各段階ごとに最大値を調べて、その最大値が答え
ans = 0
c = 0
for i in range(N+1):
    ans = max(ans, c+e[i])
    c += d[i]
print(ans)