L = int(input())

from functools import cache
#メモ化再帰
@cache
def f(remain, selected):
    if remain==1 and selected<L:
        return 1
    if selected>=L:
        return 0
    
    return sum([f(remain-1, selected+i) for i in range(1, L+1)])

print(f(12, 0))