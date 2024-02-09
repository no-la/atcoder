N = int(input())
A = list(map(int, input().split()))

#広義単調増加列を探す->そのどこかが頂点になる
ans = 1
i = 1
while i<N:
    a = [A[i-1]]
    while A[i-1]<=A[i]:
        a.append(A[i])
        i+=1
    l = len(a)
    for j in range(1, l+1):
        if a[-j]>=l-j+1>ans: #頂点の値>=頂点の左からの順番>ans
            for k in range(1, a[-j]):
                r_id = i+l-j+k
                if r_id>=N:
                    break
                if a[-j-k]<a[-j]-k or A[r_id]<a[-j]-k:
                    break
                ans = a[j]
print(ans)