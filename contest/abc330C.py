D = int(input())

ans = 100000000000000
import math
for x in range(abs(math.floor(math.sqrt(D))**2-D)+1):
    for y in range(abs(math.floor(math.sqrt(D))**2-D)+1):
        ans = min(ans, abs(x**2+y**2-D))

print(ans)