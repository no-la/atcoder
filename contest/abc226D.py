from fractions import Fraction
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

ans = set()
#街iから街jへの方向ベクトルでsetを作ればよい
for i in range(N):
    for j in range(N):
        if i==j:
            continue
        dx = XY[i][0]-XY[j][0]
        dy = XY[i][1]-XY[j][1]
        sgn = ""
        if dx<=0:
            sgn += "-"
        else:
            sgn += "+"
        if dy<=0:
            sgn += "-"
        else:
            sgn += "+"
        
        if dy!=0:
            ans.add(sgn+str(Fraction(dx, dy)))
        else:
            ans.add(sgn+"1/0")

print(len(ans))   