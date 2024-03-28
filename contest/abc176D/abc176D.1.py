from collections import deque
H, W = map(int, input().split())
C = tuple(map(lambda x: int(x)-1, input().split()))
D = tuple(map(lambda x: int(x)-1, input().split()))
S = [input() for _ in range(H)]


# 徒歩で移動できるマスを1グループとして、グループ分けする
# スタート地点のグループからゴールのグループへ行くためのワープ回数の最小値を求めたい
# グループの隣接リストを作って
# グループに対してBFSをすればよい


g = [] # g[i]: グループiに含まれるマスのリスト
gi = [[None]*W for _ in range(H)] # gi[i][j]: マス(i,j)が属するグループのid
seen = [[False]*W for _ in range(H)]

for sh in range(0, H):
    for sw in range(0, W):
        if seen[sh][sw]:
            continue
        seen[sh][sw] = True
        if S[sh][sw]=="#":
            continue
        
        #DFS
        gid = len(g)
        g.append([(sh, sw)])
        todo = deque([(sh, sw)])
        gi[sh][sw] = gid
        while todo:
            vh, vw = todo.pop()
            for dh, dw in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                h, w = vh+dh, vw+dw
                if not (0<=h<H and 0<=w<W):
                    continue
                if seen[h][w]:
                    continue
                if S[h][w]=="#":
                    continue
                g[-1].append((h, w))
                todo.append((h, w))
                gi[h][w] = gid
                seen[h][w] = True

# print("seen", *seen, sep="\n")
# print("gi", *gi, sep="\n")
# print("g", *g, sep="\n")

if gi[C[0]][C[1]]==gi[D[0]][D[1]]:
    print(0)
    exit()

# グループに対してBFSで最短距離を出す
#BFS
todo = deque([gi[C[0]][C[1]]]) # gi
dist = [None]*len(g) #todo[0]からの距離のリスト
dist[todo[0]] = 0
while todo:
    v = todo.popleft()
    for h, w in g[v]:
        for nh in range(h-2, h+3):
            for nw in range(w-2, w+3):
                if not (0<=nh<H and 0<=nw<W):
                    continue
                if gi[nh][nw]==None:
                    continue
                if dist[gi[nh][nw]]!=None: #既に調べた点は飛ばす
                    continue
                
                todo.append(gi[nh][nw])
                dist[gi[nh][nw]] = dist[v]+1
                if gi[nh][nw]==gi[D[0]][D[1]]:
                    print(dist[gi[nh][nw]])
                    exit()


print(-1)
