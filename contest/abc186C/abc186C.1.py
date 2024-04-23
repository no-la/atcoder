N = int(input())

ans = 0
for i in range(1, N+1):
    if "7" in str(i):
        continue
    else:
        temp = i
        while temp>0:
            if temp%8 == 7:
                break
            temp //= 8
            
        if temp==0:
            ans += 1
        
print(ans)
