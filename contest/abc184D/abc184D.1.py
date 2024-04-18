A, B, C = map(int, input().split())

d = []
from fractions import Fraction
from functools import cache
#メモ化再帰
@cache
def f(i, a, b, c):
    if any([x==100 for x in [a, b, c]]):
        # print(a, b, c)
        return Fraction(i)
    
    return (a*f(i+1, a+1, b, c)
            + b*f(i+1, a, b+1, c)
            + c*f(i+1, a, b, c+1)) / Fraction(a+b+c)

print(float(f(0, A, B, C)))
