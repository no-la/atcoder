N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


DA = [None]*(N+1) # DA[i]: A[DA[i][0]: DA[i][1]]がiである
DB = [None]*(N+1) # 同上
i = 0
while i<N:
    pre = A[i]
    l = i
    r = i
    while r<N and A[r]==pre:
        r += 1
    DA[A[l]] = (l, r)
    i = r
i = 0
while i<N:
    pre = B[i]
    l = i
    r = i
    while r<N and B[r]==pre:
        r += 1
    DB[B[l]] = (l, r)
    i = r
    
# print("DA", DA)
# print("DB", DB)

from collections import deque
remain = deque([[0, N]]) # reamain[_]: まだ使っていない区間
d = [None]*N
for a in range(1, N+1):
    if not DA[a]:
        continue
    if not remain:
        print("No")
        exit()
    need = DA[a][1] - DA[a][0]
    l, r = DB[a] if DB[a] else (N, -1)
    count = 0
    d[a] = []
    nremain = []
    while count<need:
        if not remain:
            print("No")
            exit()
        bl, br = remain.popleft()
        nbl, nbr = bl, br
        if l>bl+need-count:
            nbl = bl+need-count
            count = need
        else:
            if l>=bl:
                nbl = l
                count += l-bl
            if r<=br-(need-count):
                nbr = br-(need-count)
                count = need
            elif r<=br:
                    nbr = r
                    count += br-r
        d[a].append([bl, nbl])
        d[a].append([nbr, br])
        if nbl<nbr:
            nremain.append([nbl, nbr])
    for rem in nremain:
        remain.append(rem)
# print("d", *d, sep="\n")
ans_ = [[[B[i] for i in range(lr[0], lr[1])] for lr in l] for l in d if l]
# print("ans_", *ans_)
ans = []
for a in ans_:
    for b in a:
        ans += b
# print("ans", ans)
print("Yes")
print(*ans)