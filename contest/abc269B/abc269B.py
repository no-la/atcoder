S = [input() for _ in range(10)]

for a in range(1, 11):
    for b in range(a, 11):
        for c in range(1, 11):
            for d in range(c, 11):
                ans = True
                for i in range(10):
                    for j in range(10):
                        if a <= i + 1 <= b and c <= j + 1 <= d:
                            if S[i][j] != "#":
                                ans = False
                        else:
                            if S[i][j] != ".":
                                ans = False

                if ans:
                    print(a, b)
                    print(c, d)
                    exit()
