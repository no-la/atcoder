N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
S = input()
for i in range(N):
    A[i].append(S[i])

A.sort(key=lambda a: (a[1], a[0]))
# print(A)
y = 0
to_right = False
for _, b, s in A:
    if y!=b:
        y = b
        to_right = False
    
    if to_right and s=="L":
        print("Yes")
        exit()
    if s=="R":
        to_right = True
print("No")    

