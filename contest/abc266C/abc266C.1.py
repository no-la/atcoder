import math

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))


def f(X, Y):
    return (X[0] - Y[0]) ** 2 + (X[1] - Y[1]) ** 2


def area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


d = [A, B, C, D]
for i in range(4):
    j = (i - 1) % 4
    k = (i + 1) % 4

    a = math.sqrt(f(d[i], d[j]))
    b = math.sqrt(f(d[i], d[k]))
    c = math.sqrt(f(d[j], d[k]))

    S = area(a, b, c)
