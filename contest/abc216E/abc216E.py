N, K = map(int, input().split())
A = list(map(int, input().split())) + [0]

# どのアトラクションに何回ずつ乗るかを調べる気持ち
A.sort(reverse=True)
# print(A)
ans = 0
c = 1 # max(A)=A[i]なる現在のiの個数
i = 0 # そのi
remain = K
while i<N:
    # print(c, A[i], remain, ans)
    if remain-c*(A[i]-A[i+1])>=0:
        ans += c*(A[i]-A[i+1])*(A[i]+A[i+1]+1)//2
        remain -= c*(A[i]-A[i+1])
        i += 1
        c += 1
    else:
        # print(remain//c, "from", A[i], "to", A[i]-(remain//c))
        # print("and", remain%c)
        ans += c*(remain//c)*(A[i]+A[i]-(remain//c)+1)//2
        ans += (remain%c)*(A[i]-(remain//c))
        break
print(ans)
