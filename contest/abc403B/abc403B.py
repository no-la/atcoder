import sys

input = lambda: sys.stdin.readline().rstrip()
T = input()
U = input()

for i in range(len(T) - len(U) + 1):
    for j, u in enumerate(U):
        if T[i + j] == "?" or T[i + j] == u:
            continue
        else:
            break
    else:
        print("Yes")
        exit()
print("No")
