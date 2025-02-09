import sys

input = lambda: sys.stdin.readline().rstrip()
A = list(map(int, input().split()))
for i in range(3):
    j, k = (i + 1) % 3, (i + 2) % 3
    if A[i] * A[j] == A[k]:
        print("Yes")
        exit()
print("No")
