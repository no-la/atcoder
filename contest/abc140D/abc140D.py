N, K = map(int, input().split())
S = input()

# [l, r]を入れ替えると
# 0, 1, ..., l-1, r, r-1, ..., l+1, l, r+1, ..., N
# になる
# 「目の前の人」が変わるのは、l-1, r, l, r+1番目の4人だけですね
# 「目の前の人が同じ方向を向いている」必要があるので、l-1とrのどちらかとlとr+1のどちらかが変わる
# L, L, R, R, L, R, L, R, R
# 0, 1, 1, 0, 0, 0, 0, 1, 0
# 操作をするのは、R, R, ..., R or L, L, ..., Lのどちらかに対してのみ？
# 例えば、L, "R, R, L, R", L -> L, L, R, L, L, L
# 幸福なのは、1人 -> 3人
# L, "R, R", L, R, L -> L, L, L, L, R, L
# 1人 -> 3人

