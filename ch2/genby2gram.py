# -*- coding: utf-8 -*-
"""
genby2gram.pyプログラム
2-gramの連鎖により文を作成する
開始文字を指定すると文を生成します
プログラムと同じディレクトリ（フォルダ）に、text.txtという名前の
日本語ファイルを置いてください。
使い方　c:\>python genby2gram.py 
"""
# モジュールのインポート
import sys
import collections
import random

# 下請け関数の定義
# generates()関数
def generates(chr, listdata):
    """文の生成"""
    # 開始文字の出力
    print(chr, end = '')
    # 続きの出力
    while True:
        #次の文字の決定
        n = random.randint(1, listdata.count(chr)) # 検索回数の設定
        i = 0
        for k, v in enumerate(listdata):           # 文字chrを探す
            if v == chr:                           # 文字があったら
                i += 1                             # 発見回数を数える
                if i >= n:                         # 規定回数見つけたら
                    break                          # 検索終了
        nextchr  = listdata[k + 1]                 # 次の文字を設定
        print(nextchr, end = '')                   # 一文字出力
        if (nextchr == "。") or (nextchr == "．"): # 句点なら出力終了
            break
        chr = nextchr                              # 次の文字に進む
    print()                                        # 一行分の改行を出力

# generates()関数の終わり

# メイン実行部
# ファイルオープンと読み込み
f = open("text.txt",'r')
inputtext = f.read()
f.close()

# 1-gramの生成
listdata = list(inputtext)

# 開始文字の決定
startch = input("開始文字を入力してください：")

# 10回の文の生成
if startch in listdata: # 開始文字が存在するなら
    for i in range(10) :
        generates(startch, listdata)
else:                   # 開始文字が存在しない
    print("開始文字", startch, "が存在しません")

# genby2gram.pyの終わり
