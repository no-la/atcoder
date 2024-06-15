N, M, K = map(int, input().split())
NM = N*M

if not (N<=K<=NM and K&1==N&1):
    print("No")
    exit()

ans = [list("+"*(2*M-1)+"S+")]
for i in range(1, 2*N+2):
    if i&1:
        ans.append(list("+"+"o|"*(M-1)+"o+"))
    else:
        ans.append(list("+"+"-+"*M))

# あとは通りたい道を . にしていけばいい
q, r = divmod((K-N)//2, M)
for i in range(q):
    for j in range(M):
        ans[1+2*i][1+2*j] = "."
    


ans.append(list("+"*(2*M-1)+"G+"))
print("Yes")
for l in ans:
    print(*l, sep="")
