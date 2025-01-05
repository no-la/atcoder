X = input()
k = len(X)

if k <= 2:
    print(X)
    exit()


def check(num: str):
    n = len(num)
    if n > len(X):
        return True
    elif n < len(X):
        return False
    for i in range(n):
        y1, y2 = int(X[i]), int(num[i])
        if y1 < y2:
            return True
        if y1 > y2:
            return False
    return True


# まず桁数を変えずに調べる
a, b = int(X[0]), int(X[-1])
for i in range(b, 10):
    if (i - a) % (k - 1) == 0:
        t = (i - a) // (k - 1)
        ans = "".join([str(a + j * t) for j in range(k)])
        if check(ans):
            print(ans)
            exit()
for i in range(a + 1, 10):
    for l in range(10):
        if (l - i) % (k - 1) == 0:
            t = (l - i) // (k - 1)
            ans = "".join([str(i + j * t) for j in range(k)])
            print(ans)
            exit()

# 桁数を増やしながら調べる
while True:
    k += 1
    for a in range(1, 10):
        for b in range(10):
            if (b - a) % (k - 1) == 0:
                t = (b - a) // (k - 1)
                ans = "".join([str(a + j * t) for j in range(k)])
                print(ans)
                exit()
