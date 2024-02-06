S = list(input())
T = list(input())

D = {"A":0, "B":1, "C":2, "D":3, "E":4}
if (((D[S[0]]-D[S[1]])%5 in (1, 4) and (D[T[0]]-D[T[1]])%5 in (1, 4)) or
    ((D[S[0]]-D[S[1]])%5 in (2, 3) and (D[T[0]]-D[T[1]])%5 in (2, 3))):
    print("Yes")
else:
    print("No")