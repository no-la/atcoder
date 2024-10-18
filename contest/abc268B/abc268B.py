S = input()
T = input()

if len(S) <= len(T) and T[: len(S)] == S:
    print("Yes")
else:
    print("No")
