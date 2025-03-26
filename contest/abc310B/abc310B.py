import sys

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(N)]

for i, a in enumerate(d):
    for j, b in enumerate(d):
        if a[0] < b[0]:
            continue

        for x in a[2:]:
            if x not in b[2:]:
                break
        else:
            if a[0] > b[0]:
                print("Yes")
                exit()
            for x in b[2:]:
                if x not in a[2:]:
                    print("Yes")
                    exit()

print("No")
