N = int(input())

if N==1:
    print(1)
    exit()

prepre = 2
pre = 1
ans = 3
for i in range(2, N):
    prepre = pre
    pre = ans
    ans = prepre+pre
print(ans)
        
