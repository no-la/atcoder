N=int(input())  

from functools import cache
import sys

sys.setrecursionlimit
#メモ化再帰
@cache
def f(s):
    if len(s)==N:
        return set([s])
    
    rev = set()
    rev |= f(f"({s})")
    rev |= f(f"{s}()")
    rev |= f(f"(){s}")
    return rev



print(*sorted(f("()")), sep="\n")