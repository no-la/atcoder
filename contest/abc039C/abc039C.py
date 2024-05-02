S = input()

a = ["Do", "", "Re", "", "Mi", "Fa", "", "So", "", "La", "", "Si"]
d = "WBWBWWBWBWBW"*3

S = S

# for i in range(len(S)):
#     if S[i:i+12]==d:
#         print(i)
#         print(a[-i%12])
#         break

for i in range(12):
    if d[i:i+12]==S[:12]:
        print(a[i])
        break