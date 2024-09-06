N = int(input())
A = list(map(int, input().split()))

# i==A[i]を数える
c = sum([A[i]==i+1 for i in range(N)])

ans = c*(c-1)//2
# print(ans)

for i in range(N):
    j = A[i]
    if A[i]>A[j-1] and A[j-1]==i+1:
        ans += 1

print(ans)
