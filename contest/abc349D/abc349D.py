L, R = map(int, input().split())

ans = []
left = L
while left<R:
    # right を決める
    i2 = 1
    if left==0:
        i2 = 2**60
        j = 0
    else:
        while left%(i2*2)==0:
            i2 *= 2
        j = left//i2
    while i2*(j+1)>R:
        i2 //= 2
        j *= 2
    right = i2*(j+1)
    ans.append((left, right))
    left = right

print(len(ans))
for a in ans:
    print(*a)