import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
A = list(map(int, input().split()))
M = sum(A)

if M % 10 != 0:
    print("No")
    exit()

K = M // 10
A = A + A

# 尺取り法
right = 0
temp = 0
for left in range(N):
    while right < 2 * N and temp < K:
        temp += A[right]
        right += 1
    if temp == K and (right - left) <= N:
        print("Yes")
        exit()
    if left == right:  # [left, right)が空集合なので'temp=初期値'になっているはず
        right += 1
    else:  # このあとleftを+1するので、その分の情報を削る
        temp -= A[left]

print("No")
