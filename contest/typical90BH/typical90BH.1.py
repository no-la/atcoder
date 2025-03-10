import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
A = list(map(int, input().split()))

d = [1] * (N + 1)
# d[i]: 最後の要素がiであるような単調増加列の最大長
e = [1] * (N + 1)
# e[i]: 最初の要素がiであるような単調減少列の最大長
