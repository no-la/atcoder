import math
#どうしてもTLEになってしまう
#二分探索のやり方全然違いました　D2の方で通った

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
    ans = M
    i = math.ceil((ans-1)/2)
    while(True):
        if B[i] > border:
            if i == 0:
                ans = 0
                break
            elif B[i-1] > border: #左に探索
                i = math.ceil(i/2)
            else: #終了
                ans = i
                break
        else:
            if i == ans-1:
                ans = ans
                break
            elif B[i+1] < border: #右に探索
                i += math.ceil((ans-1-i)/2)
                # print(i)
            else: #終了
                ans = i+1
                break
    #print("ans", ans)
    sum_p += P*(M-ans)
    sum_a += a*ans
    sum_b += cumulative_sum_B[ans]

print(sum_p + sum_a + sum_b)