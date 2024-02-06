import math
N = int(input())
S = list(input())
S.sort()

ans = 0
#N桁以下の平方数を書き出して、Sを並べ変えて作れるかを判定する
#O(sqrt(10^N)*N)->N<=13なので最大で5*10^7くらい
#3.2秒くらいでできるらしい
for i in range(math.ceil(math.sqrt(10**N))):
    i_s = str(i**2)
    if S == sorted(list("0"*(N-len(i_s)) + i_s)):
        ans += 1

print(ans)