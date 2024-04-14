T = int(input())
INF = 10**18

for _ in range(T):
    RGB = list(map(int, input().split()))
    ans = INF
    for i in range(3): # iにあつめる
        j, k = (i+1)%3, (i+2)%3
        m, M = sorted((RGB[j], RGB[k]))
        if (M-m)%3==0:
            ans = min(ans, M)
            # print(i, (M-m)//3, ((M-m)//3)*2+m)
    print(ans if ans<INF else -1)

