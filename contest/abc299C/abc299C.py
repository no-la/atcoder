N = int(input())
S = input()
value = -1

def main():
    value = -1

    i = 0
    while(i < N-1):
        if S[i] == "o":
            for j in range(i+1, N):
                if S[j] == "-":
                    break
            else: #最後まで"-"がなかったとき
                print(value)
                return
            value = max([value, j-i])
            i = j
        else:
            if S[i+1] != "o": #--のとき
                i += 1
                continue
            for j in range(i+1, N):
                if S[j] == "-":
                    j -= 1
                    break
            value = max([value, j-i])
            i = j
    print(value)

main()
