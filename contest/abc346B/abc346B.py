W, B = map(int, input().split())
S = "wbwbwwbwbwbw"*100

for i in range(12):
    if S[i:i+W+B].count("w")==W and S[i:i+W+B].count("b")==B:
        print("Yes")
        exit()
print("No")