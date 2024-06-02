N = int(input())
A = list(map(int, input().split()))
M = 10**6
A.sort()

d = [0]*(M+1) # d[i]: sum([a<=i for a in A])
j = 0
for i in range(1, M+1):
    d[i] = d[i-1]
    while j<N and A[j]==i:
        d[i] += 1
        j += 1

# print(*A)
# print(*d)

ans = 0
for v in range(1, M+1): # A[i]==vなるiについてまとめて調べ上げる
    x = d[v]-d[v-1]
    for k in range(1, M//v+1): # 商がkになるものを数える
        kv = k*v
        c = d[min(M, kv+v-1)] - d[kv-1] # kv<=A[i]<(k+1)v を満たすiの個数
        ans += k*c*x
    # [v, 2v)を数えるときに重複して数えた分を引く
    # つまり、A[i]==vなるvを2つ選ぶ場合のうち、半分を取り除く
    ans -= x*(x+1)//2
print(ans)        
