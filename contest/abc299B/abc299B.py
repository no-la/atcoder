N, T = map(int, input().split())
input_line = input()
C = [int(i) for i in input_line.split()]
input_line = input()
R = [int(i) for i in input_line.split()]

c = -1
if T in C:
    c = T
else:
    c = C[0]
players = [i for i, x in enumerate(C) if x == c]
value = players[0]
for i in players:
    if R[value] < R[i]:
        value = i

print(value + 1)
