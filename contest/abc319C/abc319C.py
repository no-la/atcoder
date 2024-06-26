C = [list(map(int, input().split())) for _ in range(3)] 

a, b = 0, 0
# 9!=3.6x10^5 なので全探索できる
# 順列 O(nPk)<=n!
import itertools
for l in itertools.permutations(list(range(9)), 9):
    lines = [[] for _ in range(3)]
    columns = [[] for _ in range(3)]
    naname = [[] for _ in range(2)]
    for i in l:
        h, w = divmod(i, 3)
        lines[h].append(C[h][w])
        columns[w].append(C[h][w])
        if h==w:
            naname[0].append(C[h][w])
        if h==2-w:
            naname[1].append(C[h][w])
        
        if len(lines[h])==3 and lines[h][0]==lines[h][1] and lines[h][1]!=lines[h][2]:
            break
        if len(columns[w])==3 and columns[w][0]==columns[w][1] and columns[w][1]!=columns[w][2]:
            break
        if len(naname[0])==3 and naname[0][0]==naname[0][1] and naname[0][1]!=naname[0][2]:
            break
        if len(naname[1])==3 and naname[1][0]==naname[1][1] and naname[1][1]!=naname[1][2]:
            break
    else:
        a += 1
    b += 1

ans = a/b
print(ans)
