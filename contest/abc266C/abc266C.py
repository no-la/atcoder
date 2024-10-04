A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

from math import tan

d = [A, B, C, D]
for i in range(4):
    print(i)
    pre = None
    count = 0
    for t in range(i + 1, i + 4):
        j = t % 4
        if d[j][0] - d[i][0] != 0:
            now = tan((d[j][1] - d[i][1]) / (d[j][0] - d[i][0]))
        else:
            if count == 0:
                now = -float("INF")
            else:
                now = float("INF")

        print(pre, now)
        if pre is None:
            pre = now
        elif pre >= now:
            print("No")
            exit()
        else:
            pre = now

print("Yes")
