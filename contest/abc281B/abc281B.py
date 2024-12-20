S = input()
if len(S) != 8:
    print("No")
    exit()

if S[0] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    print("No")
    exit()

if S[-1] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    print("No")
    exit()

if not S[1:-1].isdigit():
    print("No")
    exit()

if not 100000 <= int(S[1:-1]) <= 999999:
    print("No")
    exit()

print("Yes")
