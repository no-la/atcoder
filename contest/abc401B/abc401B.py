import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
ans = 0
state = "logout"
for _ in range(N):
    s = input()
    if s in ["login", "logout"]:
        state = s
    else:
        if state == "logout" and s == "private":
            ans += 1

print(ans)
