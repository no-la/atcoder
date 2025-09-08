N, T = map(int, input().split())
A = list(map(int, input().split()))


def to_index(a):
    return (a - 1) // N, (a - 1) % N


line = [0] * N
column = [0] * N
diagonal = [0, 0]

for t, a in enumerate(A):
    i, j = to_index(a)
    line[i] += 1
    column[j] += 1
    if i == j:
        diagonal[0] += 1
    if i + j == N - 1:
        diagonal[1] += 1

    if line[i] == N or column[j] == N or diagonal[0] == N or diagonal[1] == N:
        print(t + 1)
        break
else:
    print(-1)
