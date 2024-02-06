import os, shutil


def file_into_folder(folder_path):
    """
    folder_path内の全てのファイルを、同じ名前のフォルダに移動する
    """
    files = os.listdir(folder_path)
    
    for f in files:
        file_path = os.path.join(folder_path, f)
        file_name = file_path.split(".")[0]
        os.makedirs(file_name)
        shutil.move(file_path, file_name)
    print("完了しました")


if __name__ == '__main__':
    file_into_folder("contest")