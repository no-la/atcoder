N = int(input())
A = list(map(lambda x: int(x)-1, input().split()))


s = None

from collections import deque
seen = [0]*N
for i in range(N):
    if seen[i]:
        continue
    
    # DFS
    todo = deque([i])
    seen[i] = True
    while todo:
        v = todo.pop()
        w = A[v]
        if seen[w]: # 既に調べた点は飛ばす
            s = w
            break
        todo.append(w)
        seen[w] = True

    if s is not None:
        break

ans = [s]
while A[ans[-1]]!=s:
    ans.append(A[ans[-1]])

print(len(ans))
print(*list(map(lambda x: x+1, ans)))
