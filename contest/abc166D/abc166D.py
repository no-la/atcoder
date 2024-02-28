X = int(input())

n = 1000
for a in range(n):
    for b in range(n):
        A = a**5
        B = b**5
        if A-B==X:
            print(a, b)
            exit()
        elif A+B==X:
            print(a, -b)
            exit()
        elif -A+B==X:
            print(-a, -b)
            exit()
            