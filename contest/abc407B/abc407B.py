import sys

input = lambda: sys.stdin.readline().rstrip()
X, Y = map(int, input().split())

bunbo = 36
bunsi = 0
for i in range(1, 7):
    for j in range(1, 7):
        bunsi += i + j >= X or abs(i - j) >= Y

print(bunsi / bunbo)
