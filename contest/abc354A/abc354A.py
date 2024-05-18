H = int(input())
i = 0
t = 0
while True:
    t += 2**i
    if t>H:
        print(i+1)
        exit()
    i += 1