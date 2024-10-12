N, X = map(int, input().split())
print(chr((X - 1) // N + ord("A")))
