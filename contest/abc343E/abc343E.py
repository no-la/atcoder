A, B, C = map(int, input().split())

v1 = 3*(7**3)
if A+B*2+C*3!=v1:
    print("No")
    exit()

a1, b1, c1 = 0, 0, 0

def f(*a):
    return max(0, min(a)+7 - max(a))


def f2(a2, b2, c2, a3, b3, c3):
    v = 0
    for x1, x2, y1, y2, z1, z2 in ((a1, a2, b1, b2, c1, c2),
                                   (a3, a2, b3, b2, c3, c2),
                                   (a1, a3, b1, b3, c1, c3)):
        v += f(x1, x2) * f(y1, y2) * f(z1, z2)
    return v
    
def f3(a2, b2, c2, a3, b3, c3):
    return f(a1, a2, a3) * f(b1, b2, b3) * f(c1, c2, c3)



import itertools
# ループ回数 15^6 = 11390625 ~ 10^7
for a2, b2, c2, a3, b3, c3 in itertools.product(range(-7, 8), repeat=6):
    v3 = f3(a2, b2, c2, a3, b3, c3)
    if v3!=C:
        continue
    v2 = f2(a2, b2, c2, a3, b3, c3)
    if v1-2*v2+3*v3!=A or v2-3*v3!=B:
        continue
    print("Yes")
    print(a1, b1, c1, a2, b2, c2, a3, b3, c3)
    exit()
print("No")
