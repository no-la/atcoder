K = int(input())
A, B = input().split()

a, b = 0, 0
for i, t in enumerate(A[::-1]):
    a += int(t)*(K**i)
for i, t in enumerate(B[::-1]):
    b += int(t)*(K**i)

print(a*b)