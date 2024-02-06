import math
H, W = map(int, input().split())
N = math.floor((min([H, W]) - 1)/2)
MAP = []
value = [0] * min([H, W])
for i in range(H):
    MAP.append(input())

def main():
    for i in range(H):
        for j in range(W):
            if MAP[i][j] == "#":
                print(f"call calc at ({i}, {j})")
                calc(i, j)
    print(" ".join(map(str, value)))

def calc(i, j):
    R = min([N, i, j, H-i-1, W-j-1])
    print(R)
    if R == 0:
        return
    for s in range(1, R + 1):
        if not (MAP[i+s][j+s] == "#" and MAP[i+s][j-s] == "#" and MAP[i-s][j+s] == "#" and MAP[i-s][j-s] == "#"):
            if s == 1:
                return
            s -= 1 #一つ余分に数えているのでもどす
            break
    print(f"value[{s - 1}] += 1")
    value[s - 1] += 1

main()