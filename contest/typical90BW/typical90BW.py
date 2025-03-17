import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())

count = -1
x = N
for i in range(2, 10**7):
    while x > 1 and x % i == 0:
        count += 1
        x //= i

ans = count.bit_length()
print(ans)
