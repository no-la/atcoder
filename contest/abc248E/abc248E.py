import fractions

N, K = map(int, input().split())
d = [tuple(map(int, input().split())) for _ in range(N)]

if K == 1:
    print("Infinity")
    exit()

ans = set()
for i in range(N):
    ax, ay = d[i]
    for j in range(i + 1, N):
        bx, by = d[j]
        # 直線ab上にある点を数える
        count = 2
        for k in range(j + 1, N):
            cx, cy = d[k]
            count += (by - ay) * (cx - ax) == (bx - ax) * (cy - ay)

        if count >= K:
            if ax == bx:
                grad = "inf"
                y_intercept = ax  # このときはx座標
            else:
                grad = fractions.Fraction(by - ay, bx - ax)
                y_intercept = -ax * grad + ay
            ans.add((grad, y_intercept))

print(len(ans))
