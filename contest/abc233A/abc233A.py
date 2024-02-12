X, Y = map(int, input().split())

import math
print(math.ceil((Y-X)/10) if Y>X else 0)