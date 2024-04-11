S = input()
N = len(S)
# 1000は8の倍数
# 下3桁を見ればいい
# 数字は1~9なので、O(9H3) = O(11C3)?
nums = []
count = [0]*10
for i in S:
    n = int(i)
    if count[n]<3:
        nums.append(n)
        count[n] += 1
# 順列 O(nPk)<=n!
import itertools
for l in itertools.permutations(nums, min(3, len(nums))):
    d = list(l)
    n = 0
    c = 1
    while d:
        n+=d.pop()*c
        c*=10
    if n%8==0:
        print("Yes")
        break
else:
    print("No")