L, R = map(lambda x:int(x)-1, input().split())
S = input()

if L==len(S)-1:
    print(S)
elif R==len(S)-1:
    t = S[L:]
    print(S[:L]+t[::-1])
else:
    t = S[L:R+1]
    print(S[:L]+t[::-1]+S[R+1:])