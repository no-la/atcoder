N, K, P = map(int, input().split())
CA = []
for i in range(N):
    CA.append(list(map(int, input().split())))

ans = [[0, [i for i in range(N)], [0]*K]] #全パラメータをi以上にするために必要なコストの最小値, [残っている案], [パラメータ]
for p in range(P):
    #初期値
    candidate = []
    #各ans[i]に対してあり得る全ての操作をDFSで調べる
    for i in range(p):
        todo = [ans[i]]
        while(len(todo) != 0):
            v = todo.pop()
            #既に実行した開発案はスルー
            if v in ans[i][1]:
                continue
            #案を実行する
            cost = v[0] + CA[v]
            for j in range(K):
                params = v[2][j] + CA[v][j]
            



print(CA)
