N = int(input())
A = list(map(int, input().split()))

for i in range(N-1):
    if A[i] != A[i+1]:
        ans = "No"
        break
else:
    ans = "Yes"
print(ans)