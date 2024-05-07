N = int(input())
S = [input() for _ in range(2)]
MOD = 1000000007

# a  aa
# a, bb の2種類の組み合わせになっている
# 順に、種類0, 1とする

# 初期化
if S[0][0]==S[1][0]:
    pre_kind = 0
    ans = 3
    i = 1
else:
    pre_kind = 1
    ans = 6
    i = 2

while i<N:
    if S[0][i]==S[1][i]:
        if pre_kind==0:
            ans = (ans*2)%MOD
        else:
            pass
        pre_kind = 0
        i += 1
    else:
        if pre_kind==0:
            ans = (ans*2)%MOD
        else:
            ans = (ans*3)%MOD
        pre_kind = 1
        i += 2

print(ans)   
