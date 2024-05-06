N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))


AB = list(zip(A, B))
CD = list(zip(C, D))


AB.sort()
CD.sort()

j = 0
fin = [False]*N
for i in range(N):
    a, b = AB[i]
    while j<M:
        c, d = CD[j]
        if a<=c and b<=d:
            j += 1
            fin[i] = True
            break
        else:
            j += 1

print("Yes" if all(fin) else "No")
