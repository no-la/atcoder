A, B, C, D, E, F, X = map(int, input().split())

t = 0
temp = 0
while temp<X:
    if temp+A>X:
        t += (X-temp)*B
        temp = X
        break
    t += A*B
    temp += C

a = 0
temp = 0
while temp<X:
    if temp+D>X:
        a += (X-temp)*E
        temp = X
        break
    a += D*E
    temp += F

print(" ")
if t>a:
    print("Takahashi")
elif t<a:
    print("Aoki")
else:
    print("Draw")
