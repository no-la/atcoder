import re
import os


def create_files(parent, number):
    dif = ["A", "B", "C", "D", "E", "F"]
    for d in dif:
        folder_path = f"{parent}\\{number}{d}"
        os.makedirs(folder_path)
        with open(f"{folder_path}\\{number}{d}.py", "w"):
            pass
        # print(f"{today}{d}.py")
    print("作成しました")


if __name__ == '__main__':
    contests = ["abc", "arc"]
    while True:
        try:
            n = input("問題番号を入力してください\n")
            if n[0:3] not in contests:
                print(f"存在しないコンテストです {n[0:3]} not in {contests}")
            elif not n[3:6].isdigit():
                print(f"問題番号は0埋めで3桁表示してください {n[3:6]}")
            else:
                break
        except ValueError:
            print("(コンテストの種類3文字)(問題番号3文字)の形で入力してください")
    create_files("contest", n)