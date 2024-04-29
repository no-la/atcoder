N = int(input())

d = [False]*(2*N+1)

for c in range(N+1):
    i = 0
    while d[i]:
        i += 1
    print(i+1)
    d[i] = True
    d[int(input())-1] = True


