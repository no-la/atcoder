# `low`と`high`の両方向に展開して、すべての回文を検索します
def expand(s, low, high, palindromes):
 
    # `s[low.high]`が回文ではなくなるまで#を実行
    while low >= 0 and high < len(s) and s[low] == s[high]:
 
        #は、すべての回文をセットにプッシュします
        palindromes.add(s[low: high + 1])
 
        #両方向に拡張
        low = low - 1
        high = high + 1
 
 
#特定の文字列のすべての一意のパリンドローム部分文字列を検索する関数
def findPalindromicSubstrings(s):
 
    #は、すべての一意のパリンドロームサブストリングを格納するための空のセットを作成します
    palindromes = set()
 
    for i in range(len(s)):
 
        #は、中点として`s[i]`を持つすべての奇数長の回文を検索します
        expand(s, i, i, palindromes)
 
        #は、`s[i]`と`s[i+1]`を持つすべての偶数の長さの回文を検索します
        # 中点としての
        expand(s, i, i + 1, palindromes)
 
    #は、すべての固有のパリンドロームサブストリングを印刷します
    return palindromes
 
 
if __name__ == '__main__':
    s = input()
    all_ = list(findPalindromicSubstrings(s))
    print(max([len(i) for i in all_]))