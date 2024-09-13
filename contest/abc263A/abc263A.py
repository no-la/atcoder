A = list(map(int, input().split()))
b = list(set(A))

s = [A.count(b[i]) for i in range(len(b))]
if s==[2, 3] or s==[3, 2]:
    print("Yes")
else:
    print("No")


