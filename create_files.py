import os


def create_files(parent, number, dif):
    """create '<number><dif>.py' at parent"""
    created_files = []
    for d in dif:
        folder_path = f"{parent}\\{number}{d}"
        if os.path.exists(folder_path):
            print(f"\033[31m{folder_path} already exits.\033[0m")
            continue
        os.makedirs(folder_path)
        file_path = f"{folder_path}\\{number}{d}.py"
        with open(file_path, "w", encoding="utf-8"):
            pass
        created_files.append(file_path)
        # print(f"{today}{d}.py")
    if created_files:
        print('-' * 15 + " created files " + '-' * 15, end="\n\n")
        print('\n'.join(created_files), end="\n\n")
        print('-' * 45)


if __name__ == '__main__':
    contests = ["abc", "arc"]
    _dif = ["A", "B", "C", "D", "E", "F"]
    is_exception_contest = False
    is_abc_or_arc_contest = False
    while True:
        try:
            n = input("問題番号を入力してください\n")
            if n == "q":
                exit()
            if n[0:3] not in contests:
                # print(f"ABC, ARC以外のコンテストです {n[0:3]} not in {contests}")
                is_exception_contest = input(f"{n}.pyを作成しますか？ y/n\n") == "y"
                if is_exception_contest:
                    break
            elif not n[3:6].isdigit():
                print(f"問題番号は0埋めで3桁表示してください {n[3:6]}")
            elif len(n) == 7 and n[6] not in _dif:
                print(f"対応していない難易度です _dif={_dif}")
            else:
                is_abc_or_arc_contest = True
                break
        except ValueError:
            print("(コンテストの種類3文字)(問題番号3文字)の形で入力してください")

    if is_abc_or_arc_contest:
        if len(n) == 7:
            contest_name = n[:-1]
            _dif = [n[-1]]
        else:
            contest_name = n
    elif is_exception_contest:
        _dif = [n[-1]]
    else:
        print("予期しないエラー")

    create_files("contest", contest_name, _dif)
