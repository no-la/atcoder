N = int(input())
A = list(map(int, input().split()))

p = 0
d = [0]*4
for a in A:
    nd = ([0]*a + d)
    nd[a] = 1
    p += sum(nd[4:])
    d = nd[:4]
print(p)
