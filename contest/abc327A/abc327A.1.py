N = int(input())
S = input()

print("Yes" if any([set((S[i], S[i+1]))==set(["a", "b"]) for i in range(N-1)]) else "No")
