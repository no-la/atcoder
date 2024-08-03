N = int(input())
A = list(map(int, input().split()))

# 桁ごとに累積和
# 30桁見れば十分
M = 1

ans = 0
for i in range(M):
    d = [0]*(N+1)
    for j in range(1, N+1):
        d[j] = d[j-1] + (A[j-1] & (1<<i))
    
    # print(*d, sep="\n")
    e = [0]*(N+1)
    # e[i]: A[i:]の累積和が奇数である区間の長さの和
    for j in range(N-1, -1, -1):
        if d[j]%2:
            e[j] = e[j+1] + 1
        else:
            e[j] = e[j+1]
    
    for j in range(1, N-1):
        ans += (2**i)*e[j]

print(ans)

