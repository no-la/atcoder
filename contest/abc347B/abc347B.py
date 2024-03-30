S = input()
N = len(S)
d = set()

for i in range(N):
    for j in range(1, N-i+1):
        d.add(S[i:i+j])

print(len(d))