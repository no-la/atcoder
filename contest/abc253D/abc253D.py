N, A, B = map(int, input().split())

import math
def f(d):
    # [1, N]にあるdの倍数の総和
    return (N//d)*(d+(N//d)*d)//2

print(f(1)-f(A)-f(B)+f(math.lcm(A, B)))
# print(f(1), f(A), f(B), f(A*B))
