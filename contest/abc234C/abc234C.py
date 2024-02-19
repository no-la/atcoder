K = int(input())

ans = []
temp = K
while temp>0:
    ans.append(str((temp%2)*2))
    temp //= 2

print("".join(ans[::-1]))