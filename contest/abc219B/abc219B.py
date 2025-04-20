import sys

input = lambda: sys.stdin.readline().rstrip()
S = [input() for _ in range(3)]
T = input()
print(*[S[int(T[i]) - 1] for i in range(len(T))], sep="")
