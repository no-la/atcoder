N = int(input())
nums = [0, 2, 4, 6, 8]
#5進数に変換すればいい
d = [] #逆向きになる
n = N-1 #0で1つずれる分
while n!=0:
    d.append(n%5)
    n //= 5

ans = 0
for i in range(len(d)):
    ans += nums[d[i]]*(10**(i))

print(ans)