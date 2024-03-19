import math
N = int(input())
A = 10**6 + 100

if N==1:
    print(0)
    exit()


# O(sqrt(N))で素因数分解
d = [0]*A
for n in range(2, A):
    while N%n==0:
        d[n] += 1
        N //= n


ans = 0

for z in d:
    if z == 0:
        continue
    ans += (-1+math.floor(math.sqrt(1+8*z)))//2
# print(d)
print(max(ans, 1))