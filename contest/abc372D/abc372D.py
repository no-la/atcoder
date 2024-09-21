N = int(input())
H = list(map(int, input().split()))

# 尺取り法
ans = []
left, right = 0, 1
temp = 0
while left < N:
    temp = H[left]
    while right + 1 < N and max(temp, H[right]) < H[right + 1]:  # 条件の判定
        temp = max(temp, H[right])
        right += 1

    for i in range(left, right):
        ans.append(right - left + 1 - (i - left))

    print(left, right)
    left = right
    right += 1

print(*ans)
