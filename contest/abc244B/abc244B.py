N = int(input())
T = input()

d = [[0, 1],[-1, 0],[0, -1],[1, 0]]
pos = [0, 0]
e = 0
for t in T:
    if t=="S":
        pos[0] += d[e][1]
        pos[1] += d[e][0]
    else:
        e += 1
        e %= 4

print(*pos)
        

