N, K, D = map(int, input().split())
A = list(map(int, input().split()))

dp = [[None]*D for _ in range(K+1)]
# dp[i][j]: i個の項のsetで、和(mod D)がjになるもののうち、和が最大のもの, その和
dp[0][0] = [[False]*N, 0]
for i in range(1, K+1):
    for j in range(D):
        max_sum, max_k = -1, None
        for k, a in enumerate(A):
            reqmod = (j-a)%D
            if dp[i-1][reqmod] is None:
                continue
            if dp[i-1][reqmod][0][k]:
                continue
            # print(i, j, k)
            temp_sum = a+dp[i-1][reqmod][1]
            if max_sum<temp_sum:
                max_sum = temp_sum
                max_k = k

        if max_k is not None:
            # print("t", dp[i-1][(j-a)%D])
            temp = dp[i-1][(j-A[max_k])%D][0].copy()
            temp[max_k] = True
            dp[i][j] = [temp, max_sum]
# print(*dp, sep="\n")
print(dp[K][0][1] if dp[K][0] is not None else -1)
