N = int(input())
H = list(map(int, input().split()))

a = H[0]
for i in range(1, N):
    h = H[i]
    if h>a:
        print(i+1)
        exit()

print(-1)
