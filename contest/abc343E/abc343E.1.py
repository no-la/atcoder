A, B, C = map(int, input().split())

v1 = 3*(7**3)

def f2(a2, b2, c2, a3, b3, c3):
    v = 0
    for x1, x2, y1, y2, z1, z2 in ((a1, a2, b1, b2, c1, c2),
                                   (a3, a2, b3, b2, c3, c2),
                                   (a1, a3, b1, b3, c1, c3)):
        xl = max(x1, x2)
        xr = min(x1, x2)+7
        yl = max(y1, y2)
        yr = min(y1, y2)+7
        zl = max(z1, z2)
        zr = min(z1, z2)+7
        v += (xr-xl)*(yr-yl)*(zr-zl)
    return v
    
def f3(a2, b2, c2, a3, b3, c3):
    xl = max(a1, a2, a3)
    xr = min(a1, a2, a3)+7
    yl = max(b1, b2, b3)
    yr = min(b1, a2, b3)+7
    zl = max(c1, c2, c3)
    zr = min(c1, c2, c3)+7
    return (xr-xl)*(yr-yl)*(zr-zl)



a1, b1, c1 = 0, 0, 0
import itertools
# ループ回数 15^6 = 11390625 ~ 10^7
for a2 in range(-7, 8):
    for b2 in range(-7, 8):
        for c2 in range(-7, 8):
            for a3 in range(-7, 8):
                for b3 in range(-7, 8):
                    for c3 in range(-7, 8):
                        v3 = f3(a2, b2, c2, a3, b3, c3)
                        if v3!=C:
                            continue
                        v2 = f2(a2, b2, c2, a3, b3, c3)
                        if v2-3*v3!=B:
                            continue
                        if v1-2*v2+3*v3!=A:
                            continue
                        print("Yes")
                        print(a1, b1, c1, a2, b2, c2, a3, b3, c3)
                        exit()
                    
    
print("No")
