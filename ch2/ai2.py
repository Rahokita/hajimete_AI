# -*- coding: utf-8 -*-
"""
ai2.py
2-gramの連鎖により文を作成する人工無脳です
プログラムと同じディレクトリ（フォルダ）に、text.txtという名前の
日本語ファイルを置いてください。
使い方　c:\>python ai2.py
"""
# モジュールのインポート
import sys
import random

# 下請け関数の定義
# generates()関数
def generates(chr, listdata):
    """文の生成"""
    # 開始文字の出力
    print(chr, end = '')
    # 続きの出力
    while True:
        # 次の文字の決定
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

# 会話しましょう
print("さくら：メッセージをどうぞ")
try:
    while True :  # 会話しましょう             
        inputline = input("あなた：")
        startch = inputline[random.randint(0,len(inputline) - 1)]
        if not (startch in listdata):  # 開始文字が存在しない 
            startch = listdata[random.randint(0,len(listdata) - 1)]
        # メッセージの作成      
        print("さくら： ", end = '')
        generates(startch, listdata)
        
except EOFError:
    print("さくら：ばいば～い")

# ai2.pyの終わり
