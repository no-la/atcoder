ab, ac, bc = input().split()

if (ab=="<" and bc=="<") or (bc==">" and ab==">"):
    print("B")
elif (ac=="<" and bc==">") or (ac==">" and bc=="<"):
    print("C")
else:
    print("A")
