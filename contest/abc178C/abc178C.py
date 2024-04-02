N = int(input())
MOD = 10**9 + 7

temp = 1
temp2 = 1
entire = 1
for i in range(N):
    temp = (temp*9)%MOD
    temp2 = (temp2*8)%MOD
    entire = (entire*10)%MOD
print((entire-(temp+temp-temp2))%MOD)