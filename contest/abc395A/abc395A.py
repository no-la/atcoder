import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
A = list(map(int, input().split()))
for i in range(N - 1):
    if A[i] >= A[i + 1]:
        print("No")
        exit()

print("Yes")
