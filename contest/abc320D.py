#DFS(深さ優先探索)
N, M = map(int, input().split())
hoge_str = "undecidable"
ans = [[hoge_str] for i in range(N)]
data = [[] for i in range(N)]

#まずはグラフを作る
for i in range(M):
    A, B, X, Y = map(int, input().split())
    data[A-1].append([B-1, X, Y])
    data[B-1].append([A-1, -X, -Y]) #辺の向きを気にしない

#DFSを行う
seen = [False]*N #各頂点に対し、検知済みかどうかを表す配列
todo = [] #検知したが訪問済みでない頂点の集合(保留中の頂点の集合) スタック
ans[0] = [0, 0]
seen[0] = True #人1は検知済み
todo.append(0)
while(len(todo) != 0):
    v = todo.pop()
    #隣接する頂点でループ
    for w in data[v]:
        #検知済みなら何もしない
        if seen[w[0]] == True:
            continue
        #頂点の座標が判明するので、計算して追加する
        ans[w[0]] = [ans[v][0]+w[1], ans[v][1]+w[2]]
        #検知済みにして、スタックに追加する
        seen[w[0]] = True
        todo.append(w[0])

print("\n".join([" ".join(map(str, s)) for s in ans]))