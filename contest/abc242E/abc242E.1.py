T = int(input())
MOD = 998244353


def f(s):
    """１つ前の文字を返す"""
    i = ord(s)
    return chr(i-1)

# 辞書順で一番Sに近い最大の回文を探せばよさそう
# 全てのNの総和は10^6なので、ここで全探索できる
for _ in range(T):
    N = int(input())
    S = input()
    
    ans = 0
    # S以下の最大の回文を探せばいい
    offset = ord("A")
    h = N//2
    tar = S[:h]
    if tar[::-1] <= S[-h:]:
            ...
    else:
        tar = tar[:-1] + f(tar[-1])
    
    if N&1==0:
        center = 1
    elif tar==S[:h]:
        center = ord(S[h])-offset+1
    else:
        ans += ord(S[h])-offset
        center = 26
    count = 0
    for i in range(h):
        count = (count+(ord(tar[i])-offset)*((26**(h-i-1)%MOD)))%MOD
        
    count += 1 # AA...A(=0)の分
    # print(S, tar, center, count)
    count = (count*center)%MOD

    ans = (ans+count)%MOD
    print(ans)
    