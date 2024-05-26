N, M = map(int, input().split())
from collections import defaultdict
d = defaultdict(list)
to_count = [0]*N
for _ in range(M):
    x, y = map(lambda x: int(x)-1, input().split())
    d[x].append(y)
    to_count[y] += 1

# root
root = None
for i in range(N):
    if to_count[i]==0:
        if root is not None:
            print("No")
            exit()
        
        root = i

# print(root, to_count)

# トポロジカルソート
from collections import deque
todo = deque([root])
A = [root]
while todo:
    v = todo.popleft()
    u = None
    for w in d[v]:
        to_count[w] -= 1
        if to_count[w] == 0:
            if u is not None:
                print("No")
                exit()
            u = w
    if u is not None:
        todo.append(u)
        A.append(u)

print("Yes")
# print(A)
B = sorted([i+1 for i in range(N)], key=lambda x: A[x-1])
print(*B)
