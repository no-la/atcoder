import sys

input = lambda: sys.stdin.readline().rstrip()
R, X = map(int, input().split())

ans = "No"
if X == 1 and 1600 <= R <= 2999:
    ans = "Yes"
if X == 2 and 1200 <= R <= 2399:
    ans = "Yes"
print(ans)
