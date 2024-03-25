a, b, c, d = map(int, input().split())

for x in range(a-3, a+4):
    for y in range(b-3, b+4):
        if (a-x)**2+(b-y)**2==5 and (c-x)**2+(d-y)**2==5:
            print("Yes")
            exit()
print("No")