N = int(input())
XY= [list(map(int, input().split())) for _ in range(N)]
A = [x+y for x, y in XY]
B = [x-y for x, y in XY]

A.sort()
B.sort()
print(max((A[-1]-A[0], B[-1]-B[0])))