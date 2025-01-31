import os


def create_files(parent, number, dif):
    """create '<number><dif>.py' at parent"""
    EXTENSIONS = ["py", "cpp"]
    templates = get_templates(EXTENSIONS)

    created_files = []
    for d in dif:
        folder_path = os.path.join(parent, f"{number}{d}")
        if os.path.exists(folder_path):
            print(f"\033[31m{folder_path} already exits.\033[0m")
            continue
        os.makedirs(folder_path)

        for e in EXTENSIONS:
            file_path = os.path.join(folder_path, f"{number}{d}.{e}")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(templates[e])
            created_files.append(file_path)
        # print(f"{today}{d}.py")
    if created_files:
        print('-' * 15 + " created files " + '-' * 15, end="\n\n")
        print('\n'.join(created_files), end="\n\n")
        print('-' * 45)


def get_templates(extensions=[]):
    rev = {}

    for e in extensions:
        with open(
            os.path.join("templates", f"template.{e}"), "r", encoding="UTF-8"
        ) as f:
            rev[e] = f.read()

    return rev


if __name__ == '__main__':
    contests = ["abc", "arc"]
    all_diffs = ["A", "B", "C", "D", "E", "F", "G"]
    is_exception_contest = False
    is_abc_or_arc_contest = False
    while True:
        try:
            contest, *diff = input("問題番号を入力してください\n").split()

            if not diff:  # 入力が無ければall_diffsで作る
                diff = all_diffs

            if contest == "q":
                exit()

            # 一応、ABC, ARC以外のときは確認をする
            if contest[0:3] not in contests:
                # print(f"ABC, ARC以外のコンテストです {n[0:3]} not in {contests}")
                is_exception_contest = (
                    input(f"{contest}{diff}を作成しますか？ y/n\n") == "y"
                )
                if is_exception_contest:
                    break
            # ABC, ARCのフォーマットチェック
            elif not contest[3:6].isdigit():
                print(f"問題番号は0埋めで3桁表示してください {contest[3:6]}")
            elif len(contest) == 7 and contest[6] not in all_diffs:
                print(f"対応していない難易度です _dif={all_diffs}")
            else:  # ここまで来たらABC, ARCのフォーマットはOK
                break
        except ValueError:
            print(
                "(コンテストの種類3文字)(問題番号3文字) [diff1] [diff2] ... の形で入力してください"
            )

    create_files("contest", contest, diff)
