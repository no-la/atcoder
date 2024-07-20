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
# print(k, c, bc)
d = (k+1)//2
a = N-bc
ans = ""
if a>=10:
    ans = str(int(str(a)[0])+1)[0]
    a = str(a)[1:]

a = str(a)
if len(a)>0:
    if a[0]=="0":
        a = "9"+a[1:]
    a = int(a) - 1
    ans += str(a)

if k%2==0:
    ans = ans+ans[::-1]
else:
    ans = ans + ans[:-1][::-1]


print(ans)