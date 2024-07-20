N = int(input())

if N<10:
    print(N-1)
    exit()
    
import math

c = 1
bc = 0
k = 0
while True:
    # print(k, c)
    k += 1
    bc = c
    c += 9*(10**(math.ceil(k/2) - 1))
    if c>=N:
        break

# 桁数はk
print(k, c, bc)
d = (k+1)//2
a = N-bc
ans = ""
for i in range(d):
    print(a)
    m = 10**(d-i-1)
    ans += str(a//m)
    a %= m

if k%2==0:
    ans = ans + ans[::-1]
else:
    ans = ans + ans[:-1][::-1]

print(ans)