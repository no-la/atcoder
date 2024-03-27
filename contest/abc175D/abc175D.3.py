N, K = map(int, input().split())
P = list(map(lambda x: int(x)-1, input().split()))
C = list(map(int, input().split()))


ans = -10**11
for s in range(N): # O(N*N)<=5000^2 = 2.5*10^7
    dist = [None]*N # dist[i]: s->iのスコア
    d = [s] # d[i]: i回移動後の頂点
    e = [None]*N # e[i]: e[i]回移動後にiに行く
    now = s
    dist[now] = 0
    e[now] = 0
    for _ in range(K):
        next_ = P[now]
        if dist[next_]==None:
            e[next_] = len(d)
            d.append(next_)
            dist[next_] = dist[now] + C[next_]
            now = next_
        else: # ループしている
            s_loop = d[e[next_]+1] # 0,1,...,0,1,...のループを1,...0ごとに管理するイメージ
            # ループ一周分のスコアのリスト
            loop_dist = [dist[i] for i in d[e[s_loop]:]]+[dist[now]+C[next_]]
            size_loop = len(loop_dist)
            break
    else:
        # ループしないとき
        ans = max(ans, max([dist[i] for i in d[1:]]))
        continue
    
    # ループするとき
    if loop_dist[-1]<=0: # ループに入る必要なし
        max_ = max([dist[i] for i in d[1:]])
    else: # ループに入る必要あり
        max_ = (
            dist[d[e[s_loop]-1]]
            + loop_dist[-1]*(K//size_loop)
            + max(loop_dist[:K%size_loop] if K%size_loop else [0]) # 空にならないようにする
                )
    
    # print(*(d[:e[s_loop]] + (d[e[s_loop]:]+[next_])*3), "...",sep="->")
    # print(f"loop : {d[e[s_loop]:]+[next_]}")
    # print(f"score out of loop : {[dist[i] for i in d[:s_loop]]}")
    # print(f"score in loop : {loop_dist}")
    # print("before loop :", dist[d[e[s_loop]-1]])
    # print("loop num :", K//size_loop)
    # print("loop remain :", K%size_loop, loop_dist[:K%size_loop])
    # print("max : ", max_)
    # print("-"*10)
    ans = max(ans, max_)
print(ans)
        
    
    