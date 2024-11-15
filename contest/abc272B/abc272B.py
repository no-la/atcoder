N, M = map(int, input().split())
d = [set(map(int, input().split()[1:])) for _ in range(M)]


for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(M):
            if i in d[k] and j in d[k]:
                break
        else:
            print("No")
            exit()

print("Yes")
