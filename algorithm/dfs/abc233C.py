#https://atcoder.jp/contests/abc233/submissions/49592873
N, X = map(int, input().split())
A = [list(map(int, input().split()))[1:] for _ in range(N)]

ans = 0
#DFS
from collections import deque
todo = deque([(0, a) for a in A[0]]) #index, seki
while todo:
    i, v = todo.pop()
    ni = i+1
    if ni>=N:
        continue
    for w in A[ni]:
        nv = v*w
        if nv<=X:
            if ni==N-1 and nv==X:
                ans += 1
            else:
                todo.append((ni, nv))
print(ans)