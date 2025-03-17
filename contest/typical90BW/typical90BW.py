import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())


count = 0
x = N
for i in range(2, 10**6 + 10):
    while x > 1 and x % i == 0:
        count += 1
        x //= i

if x > 1:
    count += 1

ans = (count - 1).bit_length()
print(ans)
