N, c1, c2 = input().split()
N = int(N)
S = list(input())

for i, s in enumerate(S):
    if s == c1:
        continue
    S[i] = c2

print("".join(S))
