N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]

#DFS
todo = [N-1] #技の番号-1
seen = [False]*N
seen[N-1] = True
ans = D[N-1][0]
while todo:
    v = todo.pop()
    for i in D[v][2:]:
        if seen[i-1]:
            continue
        todo.append(i-1)
        seen[i-1] = True
        ans += D[i-1][0]
print(ans)