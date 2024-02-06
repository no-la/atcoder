def main():
    K = int(input())

    #1桁のとき
    if K < 10:
        print(K)
        return

    #2桁以上のとき
    ans_list = []
    count = 9 #下から何番目か
    for d in range(2, 11):
        todo = [[i] for i in range(9, 0, -1)]
        while(len(todo) != 0):
            i = todo.pop()
            #print(i)
            loop = [j for j in range(i[-1]-1, -1, -1)]
            if len(i) == d-1:
                loop.reverse()
            for j in loop:
                new_i = i.copy()
                new_i.append(j)
                if len(new_i) < d:
                    todo.append(new_i)
                else:
                    count += 1
                    ans_list.append(new_i)
                    if count == K:
                        #print(ans_list)
                        ans = 0
                        for k in range(d):
                            ans += new_i[k]*(10**(d-k-1))
                        print(ans)
                        return

main()