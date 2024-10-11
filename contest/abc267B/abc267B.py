S = input()
d = [[6], [3], [1, 7], [0, 4], [2, 8], [5], [9]]

if S[0] == "1":
    print("No")
    exit()

for i in range(7):
    for si in d[i]:
        if S[si] == "1":
            break
    else:
        continue
    for j in range(i + 2, 7):
        for si in d[j]:
            if S[si] == "1":
                break
        else:
            continue
        for k in range(i + 1, j):
            for si in d[k]:
                if S[si] == "1":
                    break
            else:
                print("Yes")
                exit()

print("No")
