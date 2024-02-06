import string
N, Q = map(int, input().split())
label = list(string.ascii_uppercase[:N])

for i in range(N):
    for j in range(N - 1):
        print(f"? {label[j]} {label[j + 1]}")
        ans = input()
        if ans == ">":
            label[j], label[j + 1] = label[j + 1], label[j]


print(f"!{''.join(label)}")

#わからん！！！！