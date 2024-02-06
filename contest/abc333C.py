N = int(input())
n = 13
nums = [1]
for i in range(n-1):
    nums.append(nums[-1]*10+1)

ans = set()
#全部出してソートする
for i in range(n):
    for j in range(n):
        for k in range(n):
            ans.add(nums[i]+nums[j]+nums[k])

ans = sorted(ans)
print(ans[N-1])