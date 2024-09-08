a, b, d = map(int, input().split())

import math
deg = d*math.pi/180
ans = (a+b*1j)*(math.cos(deg)+math.sin(deg)*1j)
print(ans.real, ans.imag)
