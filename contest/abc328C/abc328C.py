N, Q = map(int, input().split())
S = input()
LR = [map(int, input().split()) for _ in range(Q)]

data = [False]*N
for i in range(N-1):
    if S[i]==S[i+1]:
        data[i] = True

nums = [0]*(N+1)#nums[i]:0~i番目までの条件を満たすものの個数
for i in range(1, N+1):
    n = 1 if data[i-1] else 0
    nums[i] = nums[i-1] + n
    
for l, r in LR:
    print(nums[r-1]-nums[l-1])