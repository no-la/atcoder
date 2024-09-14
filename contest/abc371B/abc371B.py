N, M = map(int, input().split())
d = [False]*N

for _ in range(M):
    a, b = input().split()
    a = int(a)-1
    if not d[a] and b=="M":
        d[a] = True
        print("Yes")
    else:
        print("No")
