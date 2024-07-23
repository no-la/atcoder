N = int(input())
S = input()
for i in range(N):
    if "A" in S[:i+1] and "B" in S[:i+1] and "C" in S[:i+1]:
        print(i+1)
        exit()
