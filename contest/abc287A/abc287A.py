N = int(input())
S = [input() for _ in range(N)]
print("Yes" if S.count("For") > N // 2 else "No")
