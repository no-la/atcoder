N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

if K==0:
    print(A[0])
    exit()

# 決め打ち二分探索
# O(N log(sum(A)/K)) < 2*10^5 * log(2*10^14) ~ 2*10^5 * 50 = 10^7
l = 1
r = sum(A)//K + 100
while l<r: # [r:]はできる [:l]はできない
    c = (l+r)//2 # c!=0
    count = 0
    for i in range(N):
        count += -(-A[i]//c) - 1 # 小数点以下切り上げ
        if count>K:
            break
    else:
        r = c
        continue
    l = c+1
print(l)