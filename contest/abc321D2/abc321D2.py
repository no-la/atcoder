N, M, P = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

sum_p = 0
sum_a = 0
sum_b = 0

# Bリストの累積和を事前計算
cumulative_sum_B = [0] * (M+1)
cumulative_sum_B[0] = 0
for i in range(1, M+1):
    cumulative_sum_B[i] = cumulative_sum_B[i-1] + B[i-1] #i番目はBの0からi-1番目までの和

for a in A:
    border = P - a
    #二分探索 borderを超える最小のBの元を探す
    left = -1
    right = M
    while(right-left != 1):
        mid = (left+right)//2
        if B[mid] > border:
            right = mid
        else:
            left = mid
    #print(left, right)
    sum_p += P*(M-right)
    sum_a += a*right
    sum_b += cumulative_sum_B[right]

print(sum_p + sum_a + sum_b)