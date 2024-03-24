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


# A2からは偶数個選ぶ
i1 = 0
i2 = 0
for j in range(K-2):
    if A1[i1]>=-A2[i2] and i1<len(A1):
        ans = (ans*A1[i1])%MOD
        i1 += 1
    else:
        ans = (ans*A2[i2])%MOD
        i2 += 1

# 最後の2つで符号の調整をする
if ans>0:
    if i1<len(A1)-1 and i2<len(A2)-1:
        ans = (ans*max(A1[i1]*A1[i1+1], A2[i2]*A2[i2+1]))%MOD
    elif i2<len(A2)-1:
        ans = (ans*A2[i2]*A2[i2+1])%MOD
    else:
        ans = (ans*A1[i1]*A1[i1+1])%MOD
else:
    ans = (ans*A1[i1]*A2[i2])%MOD

print(ans)