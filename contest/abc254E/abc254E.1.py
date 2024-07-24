N, M = map(int, input().split())
from collections import defaultdict
d = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    d[a].append(b)
    d[b].append(a)
Q = int(input())

seen = defaultdict(lambda: False)
ans = [[0]*4 for _ in range(N)]
from collections import deque
for s in range(N):
    # DFS
    todo = deque([[s]])
    ans[s][0] += s+1
    while todo:
        v = todo.pop()
        for w in d[v[-1]]:
            if seen[(v[-1], w)]:
                continue
            print(s, v, w)
            seen[(v[-1], w)] = True
            seen[(w, v[-1])] = True
            
            for i, a in enumerate(v[::-1]):
                ans[w][i+1] += a+1
            todo.append((v+[w])[-3:])
            seen[w] = True

print(*ans, sep="\n")

for _ in range(Q):
    x, k = map(int, input().split())
    x -= 1
    print(sum(ans[x][:k+1]))
