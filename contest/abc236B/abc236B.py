N = int(input())
A = map(int, input().split())
D = [0]*N

for a in A:
    D[a-1] += 1

for i in range(N):
    if D[i]!=4:
        print(i+1)
        exit()