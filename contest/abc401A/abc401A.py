import sys

input = lambda: sys.stdin.readline().rstrip()
S = int(input())
print("Success" if 200 <= S < 300 else "Failure")
