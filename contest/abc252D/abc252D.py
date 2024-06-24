N = int(input())
A = list(map(int, input().split()))
M = max(A)

# i<j<kであり
# A[i]==A[j]!=A[k]
# A[i]!=A[j]==A[k]
# A[k]==A[i]!=[j]
# A[i]==A[j]==A[k]
# であるものを数えればいい（これは嘘ですね）

# i<j<kについては、Aの要素3つを選んで適当に割り当てればいい

d = [0]*(M+1)
# d[i]: Aの中にあるiの個数
for a in A:
    d[a] += 1

e = [0]*(M+2) # e[i]: sum(d[:i])
for i in range(1, M+2):
    e[i] = e[i-1] + d[i-1]

ans = 0
for i in range(M+1):
    l = e[i]
    r = e[M+1] - e[i+1]
    ans += l*d[i]*r

print(ans)

