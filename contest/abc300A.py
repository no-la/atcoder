N, A, B = map(int, input().split())
nums = [int(i) for i in input().split()]

value = A + B
for i in range(N):
    if nums[i] == value:
        print(i + 1)
        break