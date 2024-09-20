R, C = map(int, input().split())

R = min(R, 15 - R + 1)
if R <= C <= 15 - R + 1:
    if R % 2:
        print("black")
    else:
        print("white")
else:
    if C % 2:
        print("black")
    else:
        print("white")
