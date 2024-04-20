N = int(input())
A = list(map(lambda x: int(x)-1, input().split()))

i = 0
ans = []
while i<N:
    # print(A)
    if A[i]!=i:
        ans.append(sorted([A[i]+1, A[A[i]]+1]))
        temp = A[i]
        A[i] = A[temp]
        A[temp] = temp
    else:
        i += 1

print(len(ans))
for a in sorted(ans):
    print(*a)
