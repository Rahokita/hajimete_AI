# -*- coding: utf-8 -*-
"""
makesnet.pyプログラム
意味ネットワークの作成
プログラムと同じディレクトリ（フォルダ）に、text.txtという名前の
日本語ファイルを置いてください。
使い方　c:\>python makesnet.py 
"""
# モジュールのインポート
import sys
import collections
import random
import re

# 下請け関数の定義
# whatch()関数
def whatch(ch):
    """字種の判定"""
    if re.match('[ァ-ンー]' , ch):#　カタカナと伸ばし棒
        chartype = 1
    elif re.match('[一-龥]' , ch):#　漢字
        chartype = 2
    else :                        #　それ以外
        chartype = 3
    return chartype
# whatch()関数の終わり

# make2gram()関数
def make2gram(text, list):
    """2-gramデータの生成"""
    morph = ""
    for i in range(len(text) - 1):
        if whatch(inputtext[i]) == 3:
            continue
        morph += text[i]
        if whatch(text[i]) != whatch(text[i + 1]):
            list.append(morph)
            morph = ""
    list.append(morph + text[-1]) 
# make2gram()関数の終わり

# makesnet()関数
def makesnet(listdata, ifpart, thenpart):
    """意味ネットワークの生成"""
    for i in range(0, len(listdata) - 1 , 2):
        ifpart.append(listdata[i])
        thenpart.append(listdata[i + 1])
# makesnet()関数の終わり

# searchsnet()関数
def searchsnet(chr, ifp, thenpart):
    """連想の生成"""
    # データのコピー
    ifpart = ifp.copy()
    # 連想の出力
    while True:
        print(chr,"は", end = '')
        #次の文字の決定
        if ifpart.count(chr) == 0: # 連想終了
            print("・・・わからない！")
            break
        n = random.randint(1, ifpart.count(chr))   # 検索回数の設定
        i = 0
        for k, v in enumerate(ifpart):             # 文字chrを探す
            if v == chr:                           # 文字があったら
                i += 1                             # 発見回数を数える
                if i >= n:                         # 規定回数見つけたら
                    break                          # 検索終了
        nextchr  = thenpart[k]                     # 次の文字を設定
        print(nextchr, "、")                       # 一文字出力
        chr = nextchr                              # 次の文字に進む
        ifpart[k] = ""
    print()                                        # 一行分の改行を出力
# searchsnet()関数の終わり

# メイン実行部
# ファイルオープンと読み込み
f = open("text.txt",'r')
inputtext = f.read()
f.close()
inputtext = inputtext.replace('\n', '')         # 改行の削除

# 形態素の2-gramデータからの、意味ネットワークの生成
listdata = [] # 形態素の2-gramデータ
make2gram(inputtext, listdata) # 2-gramデータの生成
ifpart = [] # 意味ネットワークの上位部分（条件）
thenpart = [] # 意味ネットワークの下位部分（結果）
makesnet(listdata, ifpart, thenpart) # 意味ネットワークの生成

# 開始文字列の決定
startch = input("開始文字列（形態素）を入力してください：")

# 5回の文の生成
if startch in ifpart: # 開始文字が存在するなら
    for i in range(5) :
        searchsnet(startch, ifpart, thenpart)
else:                   # 開始文字が存在しない
    print("開始文字列", startch, "が存在しません")

# makesnet.pyの終わり
