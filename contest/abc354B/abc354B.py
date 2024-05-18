N = int(input())
S = []
T = 0
for _ in range(N):
    s, c = input().split()
    S.append(s)
    T += int(c)

i = T%N
print(sorted(S)[i])
