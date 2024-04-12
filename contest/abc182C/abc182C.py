N = input()

d = [0]*3

for n in N:
    d[int(n)%3] += 1

s = (d[1]+d[2]*2)%3


if s==0:
    print(0)
elif d[s]>0 and len(N)>1:
    print(1)
elif d[3-s]>=2 and len(N)>2:
    # 2, 2 -> 1
    # 1, 1 -> 2
    print(2)
else:
    print(-1)