N, K = map(int, input().split())
P = list(map(lambda x: int(x)-1, input().split()))
C = list(map(int, input().split()))


ans = -10**11
for s in range(N): # O(N*N)
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
            print("find loop")
            print("dist", dist)
            print("d", d)
            print("e", e)
            s_loop = next_
            # ループ一周分のスコアのリスト
            loop_dist = [dist[i] for i in d[e[s_loop]:]]+[dist[now]+C[next_]]
            score_loop = dist[now]+P[next_] - dist[next_]
            size_loop = e[now]+1 - e[next_]
            break
    else:
        # ループしないとき
        ans = max(ans, max([dist[i] for i in d[1:]]))
        continue
    
    # ループするとき
    if score_loop<=0: # ループに入る必要なし
        max_ = max([dist[i] for i in d[1:]])
    else: # ループに入る必要あり
        print("start", s, "loop from", s_loop, "to", d[-1], "size", size_loop)
        print(
            dist[s_loop],
            score_loop*(K//size_loop),
            max(d[e[s_loop]:e[s_loop]+K%size_loop])
            )
        max_ = (
            dist[s_loop]
            + score_loop*(K//size_loop)
            + max(d[e[s_loop]:e[s_loop]+K%size_loop])
                )
    ans = max(ans, max_)
print(ans)
        
    
    