S = input()
N = len(S)

stack = [S[0]]
i = 1
ans = 0
while i<N:
    if stack and stack[-1]!=S[i]:
        ans += 2
        stack.pop()
    else:
        stack.append(S[i])
    i += 1

print(ans)