N = int(input())
H = list(map(int, input().split()))


ans = [0]*N
ans[0] = H[0]+1
for i in range(1, N):
    if H[i-1]>=H[i]:
        ans[i] = ans[i-1]+H[i]
    else:
        ans[i] = ans[i-1]+H[i-1]+(H[i]-H[i-1])*i


print(ans)

