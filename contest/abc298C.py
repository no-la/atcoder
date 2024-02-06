import random

TEST = True


def main():
    global N, Q, box
    N = int(input())
    Q = int(input())
    box = [[] for i in range(N)]
    ans = ""

    for k in range(Q):
        input_line = [int(i) for i in input().split()]
        if input_line[0] == 1:
            box[input_line[2]-1].append(input_line[1])
        elif input_line[0] == 2:
            box[input_line[1]-1].sort()
            ans += " ".join(map(str, box[input_line[1]-1])) + "\n"
        elif input_line[0] == 3:
            values = []
            for l in range(N): #これだとループおおすぎ　
                if input_line[1] in box[l]:
                    values.append(l+1)
            values.sort()
            ans += " ".join(map(str,values)) + "\n"
    print(ans)

def test():
    return

main()