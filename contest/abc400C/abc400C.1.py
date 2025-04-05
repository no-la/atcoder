import sys, math

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
# aの全探索

ans = 0
x = 1
while x <= N:
    x *= 2
    # bは奇数縛りで重複を消す
    temp = int(math.sqrt(N // x))
    temp -= temp // 2
    # print(x, temp)
    ans += temp


print(ans)
