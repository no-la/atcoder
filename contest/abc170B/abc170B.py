X, Y = map(int, input().split())

for a in range(X+1):
    b = X - a
    if a*4 + b*2 == Y:
        print("Yes")
        break
else:
    print("No")