S = input()
T = "ABC"

l = 0
while l+2<len(S):
    r = l+3 #[l, r)を調べる
    if S[l:r]==T:
        while True:
            if l-1>=0 and r+1<len(S) and S[l-1]+S[r:r+2]==T: #A(消えるとこ)BC
                l = l-1
                r = r+2
            elif l-2>=0 and r<len(S) and S[l-2:l]+S[r]==T: #AB(消えるとこ)C
                l = l-2
                r = r+1
            else:
                break
        S = S[:l]+S[r:]
    else:
        l += 1

print(S)