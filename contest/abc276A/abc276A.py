S = input()
print(len(S) - S[::-1].find("a") if "a" in S else -1)
