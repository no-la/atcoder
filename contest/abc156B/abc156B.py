N, K = map(int, input().split())

i = 0
temp = N
while temp>0:
    temp //= K
    i += 1
print(i)