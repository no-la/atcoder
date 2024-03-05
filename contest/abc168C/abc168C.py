A, B, H, M = map(int, input().split())

import math
print(
    math.sqrt(
        A**2+B**2-2*A*B*math.cos(
            math.pi*(60*H-11*M)/360
            )
        )
    )