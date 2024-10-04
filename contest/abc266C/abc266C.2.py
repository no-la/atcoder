import math

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

a = A[0] + A[1] * 1j
b = B[0] + B[1] * 1j
c = C[0] + C[1] * 1j
d = D[0] + D[1] * 1j

ab = b - a
ba = a - b
bc = c - b
cb = b - c
cd = d - c
dc = c - d
da = a - d
ad = d - a

tar = [[ad, ab], [ba, bc], [cb, cd], [dc, da]]
for x, y in tar:
    if (x / y).imag < 0:
        print("No")
        exit()

print("Yes")
