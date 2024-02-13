import re
import os


def create_files(parent, number, dif):
    created_files = []
    for d in dif:
        folder_path = f"{parent}\\{number}{d}"
        if os.path.exists(folder_path):
            print(f"\033[31m{folder_path} already exits.\033[0m")
            continue
        os.makedirs(folder_path)
        file_path = f"{folder_path}\\{number}{d}.py"
        with open(file_path, "w"):
            pass
        created_files.append(file_path)
        # print(f"{today}{d}.py")
    if created_files:
        print('-'*15+" created files "+'-'*15, end="\n\n")
        print('\n'.join(created_files), end="\n\n")
        print('-'*45)


if __name__ == '__main__':
    contests = ["abc", "arc"]
    dif = ["A", "B", "C", "D", "E", "F"]
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
    
    create_files("contest", n, dif)