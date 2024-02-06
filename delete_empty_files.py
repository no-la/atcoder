import os


def delete_empty_file(folder_path):
    files = os.listdir(folder_path)
    
    for f in files:
        file_path = os.path.join(folder_path, f)

        if not os.path.isfile(file_path):
            print(f"ファイルが存在しません path={file_path}")
        elif os.path.getsize(file_path)==0:
            try:
                os.remove(file_path)
                print(f"削除されたファイル: {file_path}")
            except Exception as e:
                print(f"ファイル削除中にエラーが発生しました: {file_path}, エラー: {e}")

if __name__ == '__main__':
    folder_pathes = ["contest"]
    for p in folder_pathes:
        delete_empty_file(p)