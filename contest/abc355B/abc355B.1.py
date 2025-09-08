N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
C = sorted(list(A | B))

pc = C[0]
for c in C[1:]:
    if pc in A and c in A:
        print("Yes")
        break
    pc = c
else:
    print("No")
