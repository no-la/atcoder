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
        print(scores)
        return scores[0]>scores[1]
    
    for i in range(N):
        for j in range(N):
            if d[i][j]!=-1:
                continue
            
            d[i][j] = count%2
            scores[count%2] += A[i][j]
            
            if judge(i, j):
                if d[i][j]!=0:
                    print("-"*10)
                    print(i, j)
                    print(*d, sep="\n")
                    d[i][j] = -1
                    scores[count%2] -= A[i][j]
                    return False
                else:
                    pass
            elif not f(count+1):
                d[i][j] = -1
                scores[count%2] -= A[i][j]
                return False

            d[i][j] = -1
            scores[count%2] -= A[i][j]
    
    
    return True
                

for i in range(N):
    for j in range(N):
        if (i, j)!=(1, 1):
            continue
        print(i, j)
        d[i][j] = 0
        scores[0] = A[i][j]
        if f(1):
            print("Takahashi")
            exit()
        d[i][j] = -1
        scores[0] = 0

print("Aoki")
