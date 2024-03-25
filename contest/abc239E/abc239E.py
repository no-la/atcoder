N, Q = map(int, input().split())
X = list(map(int, input().split()))
from collections import defaultdict
d = defaultdict(list)
for _ in range(N-1):
    a, b = map(lambda x: int(x)-1, input().split())
    d[a].append(b)
    d[b].append(a)


# 各頂点に、その点を根とする木に含まれる値を大きい方から20個持っておく
# 各クエリでは、根の直接の子のもつ20個の値を見ていって、K番目を返せばよい
# 直接の子をA個とすると、各クエリでO(20*A)
# Aは最大でN

# 各クエリで、ではなくて、事前に調べておけばよい？

datas = [[] for _ in range(N)] # datas[i]: 頂点iのなす木の上位20個の値
hierarchy = [] # hierarchy[i]: 深さiの頂点のリスト
childs = [[] for _ in range(N)] # childs[i]: 頂点iの直接の子

hierarchy.append([0]) # 深さ0は根のみ
# まず、葉を探す
#DFS
from collections import deque
todo = deque([(0, 0)])
seen = [False]*N #ここはsetでもよい
seen[0] = True
while todo:
    v, depth = todo.pop()
    ndepth = depth+1
    if ndepth>=len(hierarchy):
        hierarchy.append([])
    for w in d[v]:
        if seen[w]: #既に調べた点は飛ばす
            continue
        childs[v].append(w)
        hierarchy[ndepth].append(w)
        todo.append((w, ndepth))
        seen[w] = True
        
# 葉から順に、datasを埋めていく
# およそすべての頂点を2回ずつ調べてるはずなので、外側のループがO(2*N)
for l in hierarchy[::-1]:
    for v in l:
        if not childs[v]: # 子がいない
            datas[v].append(X[v])
            continue
        n = len(childs[v])
        il = [0]*n # il[j]: datas[childs[v][j]]をどこまで選んだか
        values = []
        for i in range(20): # childs[v]の各要素のdatas全体から大きいもの20個を選ぶ
            m = -1
            mi = -1
            for j in range(n): # vのj番目の子
                if il[j]>=len(datas[childs[v][j]]):
                    continue
                if m>datas[childs[v][j]][il[j]]:
                    pass
                else:
                    m = datas[childs[v][j]][il[j]]
                    mi = j
            if m==-1:
                break
            else:
                il[mi] += 1
                values.append(m)
        values.append(X[v])
        datas[v] = sorted(values, reverse=True)[:20]

for _ in range(Q):
    v, k = map(lambda x: int(x)-1, input().split())
    print(datas[v][k])