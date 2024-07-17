N = int(input())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]
Q = int(input())

from collections import deque
for _ in range(Q):
    u, v = map(lambda x: int(x)-1, input().split())
    # u->v
    dp = [[0]*(N+1) for _ in range(N)]
    dp[1][u] = A[u]
    # dp[i][j]: 長さiで最後にjにいるときのお土産の価値の最大値
    # BFS
    todo = deque([u])
    dist = [-1]*N #todo[0]からの距離のリスト
    dist[todo[0]] = 0
    while todo:
        a = todo.popleft()
        ndist = dist[a]+1
        if dist[v]!=-1 and dist[v]<ndist:
            break
        for b in range(N):
            if S[a][b]=="N":
                continue
            if dist[b]!=-1 and dist[b]<ndist: # 既に調べた点は飛ばす
                continue
            
            todo.append(b)
            dist[b] = ndist
            dp[ndist][b] = max(dp[ndist][b], dp[ndist-1][a]+A[b])
    
    if dist[v]==-1:
        print("Impossible")
    else:
        print(dist[v], dp[dist[v]][v])
        print(*dp, sep="\n")
            
            
            