N, X, Y, Z = map(int, input().split())

print("Yes" if X<=Z<=Y or Y<=Z<=X else "No")
