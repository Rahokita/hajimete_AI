# -*- coding: utf-8 -*-
"""
ai8.py
文脈を保存する人工無脳プログラム
プログラムと同じディレクトリ（フォルダ）に、text.txtという名前の
日本語ファイルを置いてください。
プログラムの終了時に、text.txtファイルを書き換えます
text.txtファイルやディレクトリの書き込み権限がないとエラーになります
使い方　c:\>python ai8.py
"""
# モジュールのインポート
import sys
import random
import re

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
        if k >= len(listdata) - 1:
            break
        nextchr  = listdata[k + 1]                 # 次の文字を設定
        print(nextchr, end = '')                   # 一文字出力
        if (nextchr == "。") or (nextchr == "．"): # 句点なら出力終了
            break
        chr = nextchr                              # 次の文字に進む
    print()                                        # 一行分の改行を出力
# generates()関数の終わり

# whatch()関数
def whatch(ch):
    """字種の判定"""
    if re.match('[ぁ-ん]' , ch):  # ひらがな
        chartype = 0
    elif re.match('[ァ-ンー]' , ch):# カタカナと伸ばし棒
        chartype = 1
    elif re.match('[一-龥]' , ch):# 漢字
        chartype = 2
    else :                        # それ以外
        chartype = 3
    return chartype
# whatch()関数の終わり

# make2gram()関数
def make2gram(text, list):
    """2-gramデータの生成"""
    morph = ""
    for i in range(len(text) - 1):
        morph += text[i]
        if whatch(text[i]) != whatch(text[i + 1]):
            list.append(morph)
            morph = ""
    list.append(morph + text[-1]) 
# make2gram()関数の終わり

# makemorph()関数
def makemorph(text, list):
    """形態素データの生成"""
    morph = ""
    for i in range(len(text) - 1):
        morph += text[i]
        if whatch(text[i]) != whatch(text[i + 1]):
            if (whatch(text[i]) == 1) or(whatch(text[i]) == 2):
                # 漢字かカタカナの並びならmorphを結合
                list.append(morph)
            morph = ""
# makemorph()関数の終わり

# メイン実行部
# ファイルオープンと読み込み
f = open("text.txt",'r')
inputtext = f.read()
f.close()
inputtext = inputtext.replace('\n', '')     # 改行の削除
morphpool = set()  # 直近の入力文からの形態素集合を初期化
# 会話しましょう
print("さくら：メッセージをどうぞ")
try:
    while True :  # 会話しましょう          
        # 形態素の2-gramデータの生成
        listdata = []
        make2gram(inputtext, listdata)
        # ユーザからの入力
        inputline = input("あなた：")
        inputlist = []
        # カタカナか漢字からなる形態素の抽出
        makemorph(inputline, inputlist)
        inputset = set(inputlist) # 形態素集合を作成
        # 開始形態素の決定
        startch = ""
        # ①直前の入力文からの選択
        while len(inputset) > 0:
            startch = inputset.pop()
            if (startch in listdata):
                break
        morphpool = morphpool | inputset
        # ②直近の入力文からの選択
        if startch == "":
            while len(morphpool) > 0:
                startch = morphpool.pop()
                if (startch in listdata):
                    break            
        # ③それ以外からの選択
        if not (startch in listdata):  # 開始形態素が存在しない 
            startch = listdata[random.randint(0,len(listdata) - 1)]
        # メッセージの作成      
        print("さくら： ", end = '')
        generates(startch, listdata)
        # 入力が句点で終わっていなければ追加する
        if not re.match('[。．]', inputline[-1] ):
            inputline = inputline + '。'
        # 生成データinputtextの更新
        inputtext = inputtext + inputline    
except EOFError:
    print("さくら：ばいば～い") 
    # ファイル書き込み処理
    f = open("text.txt",'w')
    f.write(inputtext)
    f.close()

# ai8.pyの終わり
