N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

d = [[] for _ in range(N)]
# d[i]: iと一緒に取り出せるカードの一覧
for i in range(N):
    for j in range(N):
        if i==j:
            continue
        if A[i][0]==A[j][0] or A[i][1]==A[j][1]:
            d[i].append(j)


remain = set(range(N)) # 残っているカード

def f(i): # 高橋君が勝てるかどうか
    for c1 in remain:
        for c2 in d[c1]:
            if c2 not in remain:
                continue
            # c1,c2を取り除く
            remain.discard(c1)
            remain.discard(c2)
            can_win = f(i+1)
            # もどす
            remain.add(c1)
            remain.add(c2)
            
            if not i&1 and can_win: # 高橋君が勝ちを選べる
                return True
            elif i&1 and not can_win: # 青木君が勝ちを選べる
                return False
    
    return i&1 # 手番の人が勝ちを選べないので、相手が勝つ


print("Takahashi" if f(0) else "Aoki")
