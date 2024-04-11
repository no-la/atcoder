N = int(input())

import fractions
d = []
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(len(d)):
        a1, a2 = x-d[i][0], y-d[i][1]
        c = 0
        if a2==0:
            c = 1
        else:
            a = fractions.Fraction(a1, a2)
        for j in range(i+1, len(d)):
            a1, a2 = x-d[j][0], y-d[j][1]
            if a2==0:
                if c==1:
                    print("Yes")
                    exit()
            else: 
                if a==fractions.Fraction(a1, a2):
                    print("Yes")
                    exit()
    d.append((x, y))
print("No")