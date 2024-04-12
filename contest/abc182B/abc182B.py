N = int(input())
A = list(map(int, input().split()))

ansc = -1
ans = -1
for i in range(2, max(A)+1):
    c = 0
    for a in A:
        c += (a%i==0)
    if ansc<c:
        ansc = c
        ans = i
print(ans)