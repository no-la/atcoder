N, X = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]



#BFS
from collections import deque
todo = deque([(1, a) for a in A[0][1:]]) # 袋の番号、積
ans = 0
while todo:
    i, v = todo.popleft()
    for w in A[i][1:]:
        nv = v*w
        if nv<=X:
            if i+1<N:
                todo.append((i+1, nv))
            elif i+1==N and nv==X:
                ans += 1
print(ans)