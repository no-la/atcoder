from collections import deque
N = int(input())
D = {}
for _ in range(N-1):
    u, v = map(int, input().split())
    if u not in D:
        D[u] = []
    if v not in D:
        D[v] = []
    D[u].append(v)
    D[v].append(u)

#頂点１の各分岐に存在する頂点の個数を求めて小さい方からM-1個足したものが答え
M = len(D[1])
ans = [1]*M
#頂点１が葉のときは例外として処理する
if M==1:
    print(1)
    exit()

#BFS
for i in range(M):
    todo = deque([D[1][i]]) #todo[_]:頂点番号
    seen = set([1, D[1][i]])
    while todo:
        p = todo.popleft()
        for q in D[p]:
            if q in seen:
                continue
            ans[i] += 1
            todo.append(q)
            seen.add(q)

ans.sort()
print(sum(ans[:M-1])+1)