a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))

def f(a, b):
    return a+b ==c+d or a-b == c-d or abs(a-c)+abs(b-d)<=3

if a==c and b==d:
    print(0)
elif f(a, b):
    print(1)
elif ((c-a)-(d-b))%2==0:
    print(2)
else:
    for i in range(-3, 4):
        for j in range(-3, 4):
            na, nb = a-i, b-j
            if abs(a-na)+abs(b-nb)>3:
                continue
            if f(na, nb):
                print(2)
                exit()
    print(3)