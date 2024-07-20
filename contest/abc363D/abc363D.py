N = int(input())

dp = [0, 9]
# dp[i]: i桁の回文の個数
c = 0 # 累積和
while True:
    dp.append(9*(1+dp[-2]))
    if c+dp[-1]>=N:
        break
    c += dp[-1]

print(*dp)
print(c, len(dp))

