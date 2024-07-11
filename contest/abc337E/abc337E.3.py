N = int(input())

M = 0
while 2**M<N:
    M += 1

print(M)

for i in range(M):
    a = 2**(M-i)
    tar = []
    for s in range(a//2, N, a):
        for t in range(s, min(N, s+a//2)):
            tar.append(t+1)
    print(len(tar), *tar)

S = input()

print(int(S, 2)+1)
