N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

#尺取り法
right = 0
ans = 0
for left in range(N):
    while right<N and A[right]-A[left]<M:
        right += 1
    ans = max(ans, right-left) #半開区間[left, right)の要素数

print(ans)
