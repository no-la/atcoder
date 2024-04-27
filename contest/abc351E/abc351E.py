N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]

O = [(0, 0), (0, 1)]
d = [[0, 0] for _ in range(N)]
# d[i]: 基準点からP[i]に行くための右上方向の移動回数, 右下方向の移動回数

for i in range(N):
    x, y = P[i]
    k = (x+y)%2
    dx, dy = x-O[k][0], y-O[k][1]
    sx, sy = dx//abs(dx) if dx!=0 else 0, dy//abs(dy) if dy!=0 else 0
    dx, dy = abs(dx), abs(dy)
    first = 0 if sx*sy>=0 else 1
    d[i][first] = sx*min(dx-O[k][0], dy-O[k][1])
    d[i][first-1] = sx*abs(dx-dy-O[k][dx<dy])

    print(O[k], "->", P[i], "by", d[i])

    
