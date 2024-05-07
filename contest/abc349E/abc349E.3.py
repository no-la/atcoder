N = 3
NN = N**2
A = [list(map(int, input().split())) for _ in range(N)]

d = [[-1]*N for _ in range(N)]

def judge(si, sj):
    """si,sjの色を変えたことによって縦横斜めのいずれかが揃ったかどうか調べる"""
    tar = d[si][sj]
    
    # 縦
    for i in range(1, N):
        if d[(si+i)%N][sj]!=tar:
            break
    else:
        return True
    
    # 横
    for j in range(1, N):
        if d[si][(sj+j)%N]!=tar:
            break
    else:
        return True
    
    # 斜め
    if si==sj:
        for k in range(1, N):
            if d[(si+k)%N][(sj+k)%N]!=tar:
                break
        else:
            return True
    if si+sj==N-1:
        for k in range(1, N):
            if d[(si+k)%N][(sj-k)%N]!=tar:
                break
        else:
            return True
    
    return False

scores = [0, 0]
def f(count): # 高橋が勝てるか調べる
    if count==NN:
        return scores[0]>scores[1]
    
    for i in range(N):
        for j in range(N):
            if d[i][j]!=-1:
                continue
            
            d[i][j] = count%2
            scores[count%2] += A[i][j]
            
            if judge(i, j):
                d[i][j] = -1
                scores[count%2] -= A[i][j]
                if count%2==1: # 相手の手番で、相手の勝ちが決まる
                    return False
                else: # 自分の手番で、自分の勝ちが決まる
                    return True
            
            win = f(count+1)
            d[i][j] = -1
            scores[count%2] -= A[i][j]
            if not win and count%2==1: # 相手が、自分が勝つ局面を選べる
                return False
            if win and count%2==0: # 自分の手番で、勝てる局面を選べる
                    return True
    
    return count%2==1 # 手番の人が、自分が勝つ局面を選べない(<=>相手が勝つ)
                

print("Takahashi" if f(0) else "Aoki")
