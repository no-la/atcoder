N,X,Y = map(int, input().split())

d = {}
for i in range(N-1):
    u, v = map(int, input().split())
    if u in d:
        d[u].append(v)
    else:
        d[u] = [v]
    if v in d:
        d[v].append(u)
    else:
        d[v] = [u]

seen = [False]*(N+1)
todo = [X]
route = [X]
while(True):
    v = todo.pop()
    for w in d[v]:
        if seen[w]:
            continue
        seen[w] = True
        route.append(w)
        if w == Y:
            print(route)
            exit()
        todo.append(route)
