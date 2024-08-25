N = int(input())
H = list(map(int, input().split()))

T = 0
for h in H:
    a, b = divmod(h, 5)
    T += 3*a
    while b>0:
        T += 1
        if T%3==0:
            b -= 3
        else:
            b -= 1

print(T)
