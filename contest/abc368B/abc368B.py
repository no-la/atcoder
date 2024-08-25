N = int(input())
A = list(map(int, input().split()))

ans = 0
A.sort(reverse=True)
while A[1]>0:
    A[0] -= 1
    A[1] -= 1
    A.sort(reverse=True)
    ans += 1

print(ans)
