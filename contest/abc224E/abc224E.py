from collections import defaultdict
H, W, N = map(int, input().split())
A = []
ids = []
for _ in range(N):
    r, c, a = map(int, input().split())
    r, c = r-1, c-1
    A.append((a, r, c))
    ids.append(str(A[-1]))
ans = {str(a):0 for a in A}

# aの大きい方から、最大移動回数を調べていけばよい
A.sort(reverse=True)
dr = defaultdict(list) #dr[r]:r行のaの降順リスト
dc = defaultdict(list)
for a, r, c in A:
    dr[r].append((a,r,c))
    dc[c].append((a,r,c))

for a in A:
    ia = str(a)
    for d in (dr[a[1]], dc[a[2]]):
        ib = None
        for b in d:
            if b[0]>a[0]:
                ib = str(b)
            elif ib:
                ans[ia] = max(ans[ia], ans[ib]+1)
                break
for i in ids:
    print(ans[i])

#TLE