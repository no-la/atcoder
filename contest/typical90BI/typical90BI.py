import sys

input = lambda: sys.stdin.readline().rstrip()
Q = int(input())


from collections import deque

q = deque()
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        q.appendleft(x)
    elif t == 2:
        q.append(x)
    else:
        print(q[x-1])