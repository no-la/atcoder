N = int(input())

k10 = 0
d10 = []
temp = N
while N>=10**k10:
    k10 += 1
    d10.append(temp//10)
    temp %= 10
k8 = 0
d8 = []
temp = N
while N>=8**k8:
    k8 += 1
    d8.append(temp//8)
    temp %=8

n10 = 9**(k10-1)-1
c = d10[-1] - (d10[-1]>=7)
for d in d10[-2::-1]:
    c *= d+1 - (d>=7)
n10 += c

n8 = 7**(k8-1)-1
c = d8[-1] - (d8[-1]>=7)
for d in d8[-2::-1]:
    c *= d+1 - (d>=7)
    
n810 = 0
for i in range(1, N+1):
    if "7" in str(i):
        temp = i
        while temp>0:
            if temp%8 == 7:
                n810 += 1
                break
            temp //= 8
        
print(n8, n10, n810)
print(N-n8-n10+n810)
