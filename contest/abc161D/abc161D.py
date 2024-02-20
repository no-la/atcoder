K = int(input())

count = 0
#BFS
from collections import deque
todo = deque([str(i) for i in range(1, 10)])
while todo:
    v = todo.popleft()
    count += 1
    if count==K:
        print(v)
        exit()
    for w in range(max(int(v[-1])-1, 0), min(int(v[-1])+2, 10)):
        nv = v+str(w)
        todo.append(nv)
