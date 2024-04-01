N = int(input())
A = list(map(int, input().split()))

import math
print(math.gcd(*A))