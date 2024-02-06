# ディレクトリ構造のメモ
### 全体図
atcoder  
│  
├── .vs  
├── .vscode  
├── algorithm  
├── contest  
├── directory_manager  
├── docs  
├── myclass  
├── practice  
├── .gitattributes  
├── create_files.py  
└── oj_test.ps1  

### "atcoder"
atcoder  
│  
├── .gitattributes  
├── create_files.py  
└── oj_test.ps1  

- create_files.py
    - コンテストに必要なディレクトリを作る
    - コンテスト前に一度実行する
- oj_test.ps1
    - 自動テスト、自動提出用
    - ctrl+shift+a : 自動テスト
    - ctrl+shift+q : 自動提出


### "algorithm"
atcoder  
│  
├── algorithm  
│   ├── bfs  
│   ├── dfs  

アルゴリズムやデータ構造の例題や解釈などを置く


### "contest"
atcoder  
│  
├── contest  
│   ├── abc000A  
│   │   ├── samples  
│   │   │   ├── sample-1.in  
│   │   │   ├── sample-1.out  
│   │   │   ├── sample-2.in  
│   │   │   ├── sample-2.out  
│   │   └── abc000A.py  

atcoderのabc, arcなどのコンテストの解答を置く

- samples
    - 先述のoj_test.ps1によるテストデータを置く


### "directory_manager"
ディレクトリ構造を管理するためのスクリプトを置く


### "myclass"
atcoder  
│  
├── myclass  
│   ├── mod_functions.py  

コンテスト中にデバッグのために使うメソッドやクラスなどを置く


### "practice"
その他の練習用のファイルを置く