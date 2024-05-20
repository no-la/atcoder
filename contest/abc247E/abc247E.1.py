N, X, Y = map(int, input().split())
A = list(map(int, input().split()))


# Xより大きいもの、Yより小さいものを含まない最大の部分列
# X, Yを含む最小の部分列
# の2つを調べる


# Xより大きいもの、Yより小さいものを含まない最大の部分列
# を調べて、その中にある最も近いX, Yの位置がわかればいい
l, r = 0, 0
xpos = []
ypos = []
while r<=N:
    while X<=A[r]<=Y:
        ...

