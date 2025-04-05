import sys, math

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
# aの全探索

ans = 0
a = 2
while a <= N:
    # bは奇数縛りで重複を消す
    temp = int(math.sqrt(N / a))
    for b in range(temp + 100, max(0, temp - 100), -1):
        if a * b * b <= N:
            break
    ans += (b + 1) // 2
    a *= 2


print(ans)
