import sys

input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())
A = list(map(int, input().split()))
M = max(A)

# d[i]: 整数iがAの元の約数として何回現れるか, がつくれればいい？
# aの約数xのうち、d[x]>=Kなる最大のものが答え
# 10^6以下で最も約数が多い数字は？ -> 多分 2*3*5*7*11*13 で、約数は2^6=64個
# 違うわ。4*9*25*49=44100 は 3^4=81個
# 2^3*3*5*7*11*13=840840 は 2^7=128個
# 2^4*3^2*5*7*11*13=720720 は 5*3*2^4=240個
# まあ多分O(100)程度になる？

divisors = [set() for _ in range(M + 1)]
# divisors[a]: aの約数
count = [0] * (M + 1)
# count[x]: 約数としてxが現れる回数

# O(M*logM)
for i in range(1, M + 1):
    for x in range(i, M + 1, i):
        divisors[x].add(i)

# print(*divisors, sep="\n")
