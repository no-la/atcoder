X = input()
N = len(X)

ans = [] #各桁の数字
temp = 0
for i in range(N):
    temp += int(X[i])
    ans.append(temp)

# 繰り上がり
for i in range(N-1, 0, -1):
    ans[i-1] += ans[i]//10
    ans[i] = ans[i]%10

print("".join(map(str, ans)))