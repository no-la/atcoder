N, K = map(int, input().split())
A = list(map(int, input().split()))

MOD = 10**9 + 7

A1 = []
A2 = []
ZERO = 0
for a in A:
    if a>0:
        A1.append(a)
    elif a<0:
        A2.append(a)
    else:
        ZERO += 1

A1.sort(reverse=True)
A2.sort()


ans = 1

# 答えが正でないとき
if (not A1 and K%2) or (K==N and len(A2)%2) or (N-ZERO<=K):
    if ZERO>0:
        print(0)
    else:
        i1 = 0
        i2 = 0
        for _ in range(K):
            if i1==len(A1) or (i2<len(A2) and A1[i1]>=-A2[i2]):
                a = A2[-i2-1]
                i2 += 1
            else:
                a = A1[i1]
                i1 += 1
            ans = (ans*a)%MOD
        print(ans)
    exit()


if K==1:
    print(A1[0])
    exit()


i1 = 0
i2 = 0
for j in range(K-2):
    if A1[i1]>=-A2[i2] and i1<len(A1):
        ans = (ans*A1[i1])%MOD
        i1 += 1
    else:
        ans = (ans*A2[i2])%MOD
        i2 += 1

temp1 = 0
temp2 = 0
for i in range(3): # A1からi個選ぶ
    temp = 1
    if i1+i>len(A1) or i2+2-i>len(A2):
        continue
    for j in range(i1, i1+i):
        temp *= A1[j]
    for j in range(i2, i2+2-i):
        temp *= A2[j]
    temp1 = max(temp1, temp)
    temp2 = min(temp2, temp)

temp1 %= MOD
temp2 %= MOD

print((ans*temp1 if ans>0 else ans*temp2)%MOD)