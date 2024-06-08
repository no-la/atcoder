S = input()
c = sum([s.islower() for s in S])

print(S.lower() if c>len(S)//2 else S.upper())