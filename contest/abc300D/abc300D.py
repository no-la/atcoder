import math
N = int(input())
P = [2, 3] #10^3までの素数
P_NUM = 27293
for i in range(5, 316227):
    for j in range(2, math.floor(math.sqrt(i)) + 1):
        if i % j == 0:
            break
    else:
        P.append(i)
value = 0
def main():
    global value, P_NUM, N
    for i in range(0, P_NUM):
        if P[i]**5 >= N:
            break
        for j in range(i+1, P_NUM):
            if 2 * P[i]**3 >= N:
                break
            for k in range(j+1, P_NUM):
                if not (P[i]**2 * P[j] * P[k]**2 <= N):
                    break
            value += k - j
    print(value)

main()