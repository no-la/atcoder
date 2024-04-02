S = int(input())
MOD = 10**9 + 7


import math
# 先に3を振り分けてから、残りを自由に振り分ける
ans = 0
for i in range(1, S//3 + 1): # i: 項数
    r = S-i*3
    ans = (ans+math.comb(r+i-1, i-1))%MOD
print(ans)