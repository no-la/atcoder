import sys

input = lambda: sys.stdin.readline().rstrip()
N, B = map(int, input().split())

# f(m)の全探索
# およそ、$O(11! + 10! + ... + 1!)=43954713 ~ 4*10^7
# いや違うわ
# わからないかも
