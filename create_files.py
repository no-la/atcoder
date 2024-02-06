import re

def create_files(parent, date):
    dif = ["A", "B", "C", "D", "E", "F"]
    for d in dif:
        open(f"{parent}\\{date}{d}.py", "w")
        # print(f"{today}{d}.py")
    print("作成しました")

if __name__ == '__main__':
    print("今日のコンテストですか？ y/n")
    if input()=="y":
        folder_path = "contest"
    else:
        folder_path = "practice"
        
    print("問題番号を入力してください")
    date = input()
    create_files(folder_path, date)