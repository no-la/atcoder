N, S = map(int, input().split())
A = list(map(int, input().split()))

sa = sum(A)
S %= sa

left = set([sa])
right = set([0])

temp = 0
for i in range(N):
    temp += A[i]
    right.add(temp % sa)
temp = sa
for i in range(N):
    temp -= A[i]
    left.add(temp % sa)

for l in left:
    for offset in range(-3, 4):
        if S - l + offset * sa in right:
            print("Yes")
            exit()

# print(left, right, S, sep="\n")
print("No")
