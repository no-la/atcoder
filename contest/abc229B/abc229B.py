A, B = input().split()
n = min(len(A), len(B))
for i in range(1, n+1):
    if int(A[-i])+int(B[-i])>=10:
        print("Hard")
        break
else:
    print("Easy")