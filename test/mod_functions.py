#modの逆算
def find_rations_from_mod(x, d, m=998244353):
    #https://rsk0315.hatenablog.com/entry/2023/04/29/043512
    #xq=p (mod m)となるp,qを求める
    #dはp,qの一意性を保障するためのもの
    #p,qは|p|<[m/2d], 0<q<dの条件下で一意に定まる
    n = m/(2*d)
    #stern_brocot木で探索して、条件を満たすものを見つける
    fractions = [(0, 1), (1, 1)]
    count = 0
    while(True):
        i = fractions[0][0] + fractions[1][0]
        q = fractions[0][1] + fractions[1][1]
        p = q*x-i*m
        if abs(p)<n and q<d:
            return f"{p}/{q}"
        #|p|<nとしたいので、pは0に近づいていけばよい
        #p=qx-imより、i/qとpは反比例する
        if p<0:
            fractions[1] = (i, q)
        elif p>0:
            fractions[0] = (i, q)
        else:
            return None

        count += 1
        print(count, f"{p}/{q}")
        if count > 1000000:
            break

def stern_brocot(l_x, l_y, r_x, r_y):
    #https://tjkendev.github.io/procon-library/python/math/stern-brocot-tree.html
    #開区間(l_x/l_y,r_x/r_y)内の分数を探索する
    fractions = [(l_x, l_y), (r_x, r_y)]
    for i in range(10):
        temp = fractions.copy()
        n = len(fractions)
        for j in range(n-1):
            x = temp[j][0] + temp[j+1][0]
            y = temp[j][1] + temp[j+1][1]
            if y > i+1:
                continue
            fractions.insert(j-n+1, (x, y))
    
    #デバッグ用
    # s = ""
    # for f in fractions:
    #     s += "/".join(map(str, f))+" "
    # print(s)
    return fractions


# stern_brocot(0, 1, 1, 1)
# mod = 998244353
# p = 7
# q = 100
# x = (pow(q, -1, mod)*p%mod)

# ans = find_rations_from_mod(x, 1000, mod)
# print(ans)