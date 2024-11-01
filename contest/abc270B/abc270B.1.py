X, Y, Z = map(int, input().split())

# 直接ゴール
if 0 < X < Y or Y < X < 0 or X < 0 < Y or Y < 0 < X:
    print(abs(X))
elif 0 < Z < Y or Y < Z < 0 or Z < 0 < Y or Y < 0 < Z:  # ハンマー拾ってゴール
    print(abs(Z) + abs(X - Z))
else:
    print(-1)
